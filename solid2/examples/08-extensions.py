#! /usr/bin/env python

from solid2 import *
from solid2.core.object_base import OpenSCADObject, ObjectBase,\
                                    AccessSyntaxMixin, OperatorMixin

# ==============
# = Extensions =
# ==============
# expsolid is extendable through extensions. This (and the next) example show
# some usage of it.

# add a simple functions as access syntax extension
@register_access_syntax
def leftUp(obj, x=1):
    return obj.left(x).up(x)

# create a custom OpenSCADObject that maps to color(c="red")
# and register it as access syntax extension
@register_access_syntax
class red(OpenSCADObject):
    def __init__(self):
        super().__init__(name="color", params={"c" : "red"})

# a non sense object that's not an OpenSCADObject. You can use this to get
# "low-level" access if you don't want the typical OpenSCAD
# call(params)(children) syntax. For example the debug,background,.... modifiers
# are implemented like this (see core/builtins.py)
@register_access_syntax
class non_sense_comment(ObjectBase, AccessSyntaxMixin, OperatorMixin):
    def _render(self):
        return "//non sense comment\n" + super()._render()

# A pre render extension. This hooks it into the "_render" routine. It will be
# called before the root node gets rendered. As a result you should(!) even be
# able to manipulate the whole tree (this is untested!), but at least to extract
# information from it, process it and use it to generate header contents
@register_pre_render
def non_sense_pre_render(root):

    def count_nense_recursive(node):
        count = 0
        if isinstance(node, non_sense_comment):
            count += 1

        for c in node._children:
            count += count_nense_recursive(c)

        return count

    count = count_nense_recursive(root)
    return f"//the root tree contains {count} non sense comment(s)\n"

# ==============

# old school syntax
cube1 = non_sense_comment()(
            red()(
                leftUp(
                    cube(10)
                )
            )
        )

# access style syntax
cube2 = cube(5).leftUp(3).red().non_sense_comment()

(cube1 + cube2).save_as_scad()

# This generates the following output:
#
#
# //the root tree contains 2 non sense comment(s)
#
# union() {
#         //non sense comment
#         color(c = "red") {
#                 translate(v = [0, 0, 1]) {
#                         translate(v = [-1, 0, 0]) {
#                                 cube(size = 10);
#                         }
#                 }
#         }
#         //non sense comment
#         color(c = "red") {
#                 translate(v = [0, 0, 1]) {
#                         translate(v = [-1, 0, 0]) {
#                                 cube(size = 5);
#                         }
#                 }
#         }
# }
