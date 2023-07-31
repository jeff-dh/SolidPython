#! /usr/bin/env python

from solid2 import *
from solid2.core.object_base import OpenSCADObject, ObjectBase

# ==============
# = Extensions =
# ==============
# expsolid is extendable through extensions. This (and the next) example show
# some usage of it.

# create a custom OpenSCADObject that maps to color(c="red")
class red(OpenSCADObject):
    def __init__(self):
        super().__init__(name="color", params={"c" : "red"})

# a non sense object that's not an OpenSCADObject. You can use this to get
# "low-level" access if you don't want the typical OpenSCAD
# call(params)(children) syntax. For example the debug,background,.... modifiers
# are implemented like this (see core/builtins.py)
class non_sense_comment(ObjectBase):
    def _render(self):
        return "//non sense comment\n" + super()._render()

# A pre render extension. This hooks it into the "_render" routine. It will be
# called before the root node gets rendered. As a result you should(!) even be
# able to manipulate the whole tree (this is untested!), but at least to extract
# information from it, process it and use it to generate header contents
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

# register the pre render extension.
from solid2.core.extension_manager import default_extension_manager
default_extension_manager.register_pre_render(non_sense_pre_render)

# add an access syntax extension
def leftUp(x):
    return x.left(1).up(1)

# register the access syntax extension
default_extension_manager.register_access_syntax(leftUp)

# register red as access syntax extension
default_extension_manager.register_access_syntax(red)
# ==============


cube1 = cube(10).red()
cube2 = cube(5).leftUp()

commented_cube1 = non_sense_comment()(
                      cube1
                  )
# OpenSCAD-style syntax:
red_commented_cube1 = red()(
                          commented_cube1
                      )

commented_cube2 = non_sense_comment()(
                        cube2
                    )

scene = red_commented_cube1 + commented_cube2
scene.save_as_scad()

# This generates the following output:
#
#
#     //the root tree contains 2 non sense comment(s)
#
#     union() {
#         color(c = "red") {
#             //non sense comment
#             cube(size = 10);
#         }
#         //non sense comment
#         translate(v = [-20, 0, 0]) {
#             cube(size = 5);
#         }
#     }
