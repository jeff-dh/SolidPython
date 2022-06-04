from ...core.object_base import ObjectBase
from ...core.utils import indent
from ...core.extension_manager import default_extension_manager

# the hole extension this enables to use
#   hole()(.....) in python
class hole(ObjectBase):
    def _render(self):
        #override the _render function so we don't render the hole
        #in the regular rendering process
        return ""

    def _render_hole(self):
        #render the holes when (a part) traverses the tree again
        #to render all holes
        return super()._render()

# the part extension this enable to use
#   part()(...)
# it is a RootExtension because we also inject it 
class part(ObjectBase):
    def _render(self):
        part_str = ""

        #render ("regular") children, holes will not be rendered (-> hole._render())
        for child in self.children:
            part_str += child._render()

        #render holes
        holes_str = find_and_render_child_holes(self.children)
        if len(holes_str):
            holes_str = "/* Holes below */\n" + holes_str

        #if there are holes below this node.....
        if len(holes_str):
            #substract the holes from the part
            part_str = 'difference(){ //part hole extension\n' + indent(part_str + holes_str ) + '\n}\n'

        return part_str


#inject a root extension, e.g. wrap an instancen of this class around
#the root node before rendering it. Equals python code:
#       part(root_node)
default_extension_manager.register_root_wrapper(lambda root : part()(root))

# ==========================
# = local helper functions =
# ==========================
def is_hole(obj):
    return isinstance(obj, hole)

def is_part(obj):
    return isinstance(obj, part)

def find_and_render_child_holes(childs):
    holes_str = ""

    # traverse children
    for c in childs:
        #if child is a hole, render it
        if is_hole(c):
            holes_str += indent(c._render_hole())

        #->if child is not a hole
        else:
            #and not a part (this allows "multiparthole")
            if not is_part(c):
                #recursiv call to traverse each child
                child_holes_str = find_and_render_child_holes(c.children)
                #if in the child sub tree where holes
                if child_holes_str != '':
                    #render "self" around the child
                    holes_str += c.generate_scad_head() + "{" + indent(child_holes_str) + "\n}"

    return holes_str

