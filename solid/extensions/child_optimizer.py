from solid import *
from solid.core.object_base import scad_inline, ObjectBase

class DepthMap:
    def __init__(self):
        self.data = []
        self.nodeSet = set()
        self.iter_idx = -1
        self.iter_list = []

    def addNode(self, node, depth):
        if len(self.data) < depth+1:
            assert(len(self.data) == depth)
            self.data.append([])
        assert(len(self.data) >= depth+1)
        self.data[depth].append(node)

    def __iter__(self):
        iter_set = set()
        self.iter_list = []
        for i in range(len(self.data)):
            idx = len(self.data)-i-1

            for n in self.data[idx]:
                if not n in iter_set:
                    iter_set.add(n)
                    self.iter_list.append(n)
        self.iter_idx = len(self.iter_list)-1
        return self

    def __next__(self):
        if self.iter_idx == -1:
            raise StopIteration
        d = self.iter_list[self.iter_idx]
        self.iter_idx -= 1
        return d

def childOptimizer(root):
    import copy
    root = copy.deepcopy(root)
    depthMap = DepthMap()
    nodeReferenceCount = {}
    nodeParents = {}

    #collect nodeRefereneCount and nodeParents dicts
    def collectData(node, parent=None, depth=0):

        depthMap.addNode(node, depth)
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

        for c in node.children:
            collectData(c, node, depth)

    collectData(root)

    #extract the nodes we want to extract as children
    childsToExtract = [n for n in depthMap if nodeReferenceCount[n] > 1]
    getChildId = lambda n : len(childsToExtract) - childsToExtract.index(n) - 1

    #replace the reference to the objects with calls to children(id)
    for n in childsToExtract:
        parents = nodeParents[n]
        #replace the references in each parent
        for p in parents:
            while p.children.count(n) > 0:
                idx = p.children.index(n)
                p.children[idx] = scad_inline(f"children({getChildId(n)});\n")

    #create wrapper object and fill it
    mainModule = ObjectBase()
    #add the mainModule wrapper
    mainModule(scad_inline("module wrapperModule0() {\n"))
    #fill its body with the (modified) root node)
    mainModule(root)
    mainModule(scad_inline("}\n"))

    #render all the childs
    for n in childsToExtract:
        idx = childsToExtract.index(n)
        mainModule(scad_inline(f"module wrapperModule{idx+1}() {{\n"))
        #the call to the next wrapperModule
        mainModule(scad_inline(f"wrapperModule{idx}(){{"))
        #pass on all the childs
        for i in range(len(childsToExtract) - idx - 1):
            mainModule(scad_inline(f"children({i});"))
        #render the "new child" in the chain
        mainModule(n)
        mainModule(scad_inline("}}\n"))

    #call the last wrapperModule
    mainModule(scad_inline(f"wrapperModule{len(childsToExtract)}(){{}};\n"))

    return mainModule

#register this extension
from solid.core.extension_manager import default_extension_manager
default_extension_manager.register_root_wrapper(childOptimizer)
