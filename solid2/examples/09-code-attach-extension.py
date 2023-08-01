#! /usr/bin/env python

from pathlib import Path

from solid2 import *

# =============
# = Extension =
# =============
# This is more or less the same as -- regular -- SolidPython does when it
# writes a scad file. It appends the python source to the end of the *.scad
# file.
#
# If you like this, you can simply import this extension that should do it.
#
# register the post_render extension using the decorator. This hooks it into
# the "_render" routine. It will be called after the root gets rendered. It's
# return string will be appended to the rendered string.
@register_post_render
def attach_code_post_render(root):
    #find the "root" file
    calling_file = None

    import __main__
    # not called from a terminal?
    if hasattr(__main__, "__file__"):
        # extract filename and replace suffix
        calling_file = Path(__main__.__file__).absolute()
    else:
        return '' # no code available. Called from withing a python shell

    assert(calling_file.exists())

    # read source file
    with calling_file.open("r") as f:
        code_str = f.read()

        # escape /* and */ because otherwise it would end this comment block which
        # we use to inject the solid code
        code_str = code_str.replace("/*", "/_*")
        code_str = code_str.replace("*/", "*_/")

        # return the string to be appended to the *.scad file
        return f'/* Generated from the following ExpSolid code:\n\n' +\
               f'{code_str}*/'

# =============

if __name__ == "__main__":
    c = cube(10)
    c.save_as_scad()

