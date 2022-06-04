from solid import *
from solid.core.object_base import OpenSCADConstant, ObjectBase

def childOptimizer(root):
    nodeReferenceCount = {}
    nodeParents = {}

    #collect nodeRefereneCount and nodeParents dicts
    def collectRefCountAndParents(node, parent=None, indent=""):
        nonlocal nodeParents
        nonlocal nodeReferenceCount

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

        #print(f"{indent}{node.name}:{id(node)}")
        indent += "--"
        for c in node.children:
            collectRefCountAndParents(c, node, indent)

    collectRefCountAndParents(root)


    #extract the nodes we want to extract as children
    childsToExtract = [n for n in nodeReferenceCount.keys() if nodeReferenceCount[n] > 1]
    getChildId = lambda n : childsToExtract.index(n)

    #replace the reference to the objects with calls to children(id)
    for n in childsToExtract:
        #print(f"{n.name} refCount: {nodeReferenceCount[n]}")
        #print(f"!!!{getChildId(n)}")
        parents = nodeParents[n]
        #replace the references in each parent
        for p in parents:
            #this is to prevent a bug and causes issues!
            #otherwise we get issues with nested children!
            #TODO: I don't know what this means..... wrong algorithm???
            #      do we need a recursiv approach?
            #if p in childsToExtract:
            #    continue
            while p.children.count(n) > 0:
                idx = p.children.index(n)
                p.children[idx] = OpenSCADConstant(f"children({getChildId(n)});\n")

    #for n in childsToExtract:
    #    print(f"child{getChildId(n)} {n._render()}")

    #create wrapper object and fill it
    mainModule = ObjectBase()
    #add the mainModule wrapper
    mainModule(OpenSCADConstant("module mainModule() {\n"))
    #fill its body with the (modified) root node)
    mainModule(root)
    #...
    mainModule(OpenSCADConstant("}\n"))

    #the call to the mainModule wrapper
    mainModule(OpenSCADConstant(f"mainModule(){{"))

    #render all the childs
    for n in childsToExtract:
        mainModule(n)
    #...
    mainModule(OpenSCADConstant("}\n"))

    return mainModule

#register this extension
from solid.core.extension_manager import default_extension_manager
default_extension_manager.register_root_wrapper(childOptimizer)


#test model 1
c = cube(2)
m1 = cube(1) + sphere(2)
m2 = circle(5) + c + c #m1
model1 = m1 - m2 + m1.translateX(10)

#test model 2
c = cube(1)
model2 = c + c

#render
print(model1)
