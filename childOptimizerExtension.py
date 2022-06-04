from solid import *
from solid.core.object_base import OpenSCADConstant, ObjectBase

def childOptimizer(root):
    #print(root._render())
    depthMap = []
    nodeReferenceCount = {}
    nodeParents = {}

    #collect nodeRefereneCount and nodeParents dicts
    def collectRefCountAndParents(node, parent=None, depth=0):
        nonlocal nodeParents
        nonlocal nodeReferenceCount

        if len(depthMap) < depth+1:
            assert(len(depthMap) == depth)
            depthMap.append([])
        assert(len(depthMap) >= depth+1)
        depthMap[depth].append(node)
        depth += 1

        if not node in nodeParents:
            nodeParents[node] = set()
        if not node in nodeReferenceCount:
            nodeReferenceCount[node] = 0

        if not parent in nodeParents[node]:
            if parent != None:
                nodeReferenceCount[node] += parent.children.count(node)
            else:
                nodeReferenceCount[node] += 1

        if parent != None:
            nodeParents[node].add(parent)

        #print(f"{depth * 2 * "-"}{node.name}:{id(node)}")
        for c in node.children:
            collectRefCountAndParents(c, node, depth)

    collectRefCountAndParents(root)

    #extract the nodes we want to extract as children
    childsToExtract = [n for n in nodeReferenceCount.keys() if nodeReferenceCount[n] > 1]
    getChildId = lambda n : len(childsToExtract) - childsToExtract.index(n) - 1

    #replace the reference to the objects with calls to children(id)
    #for n in childsToExtract:
    depthMap.reverse()
    visitedNodes = []
    for d in depthMap:
        for n in d:
            if n in visitedNodes:
                continue
            visitedNodes.append(n)
            if not n in childsToExtract:
                continue
            #print(f"{n.name} refCount: {nodeReferenceCount[n]}")
            #print(f"!!!{getChildId(n)}")
            parents = nodeParents[n]
            #replace the references in each parent
            for p in parents:
                while p.children.count(n) > 0:
                    idx = p.children.index(n)
                    p.children[idx] = OpenSCADConstant(f"children({getChildId(n)});\n")

    #create wrapper object and fill it
    mainModule = ObjectBase()
    #add the mainModule wrapper
    mainModule(OpenSCADConstant("module wrapperModule0() {\n"))
    #fill its body with the (modified) root node)
    mainModule(root)
    #...
    mainModule(OpenSCADConstant("}\n"))

    #render all the childs
    for n in childsToExtract:
        idx = childsToExtract.index(n)
        mainModule(OpenSCADConstant(f"module wrapperModule{idx+1}() {{\n"))
        #the call to the next wrapperModule
        mainModule(OpenSCADConstant(f"wrapperModule{idx}(){{"))
        #pass on all the childs
        for i in range(len(childsToExtract) - idx - 1):
            mainModule(OpenSCADConstant(f"children({i});"))
        #render the "new child" in the chain
        mainModule(n)
        mainModule(OpenSCADConstant("}}\n"))

    #call the last wrapperModule
    mainModule(OpenSCADConstant(f"wrapperModule{len(childsToExtract)}(){{}};\n"))

    return mainModule

#register this extension
from solid.core.extension_manager import default_extension_manager
default_extension_manager.register_root_wrapper(childOptimizer)


#test model 1
c = cube(2)
m1 = cube(1) + sphere(2)
m2 = circle(5) + c + c + m1
model1 = m1 - m2 + m1.translateX(10)

#test model 2
c = cube(1)
model2 = c + c

#render
print(model1)
