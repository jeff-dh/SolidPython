from functools import singledispatch

from ..core import builtins

def extract_size_list(size_count, *args):
    if len(args) <= 1:
        return args

    size_list = []
    args_copy = list(args)

    while args_copy and len(size_list) < size_count:
        a = args_copy.pop(0)
        if type(a) == int or type(a) == float:
            size_list += [a]
        else:
            args_copy = [a] + args_copy
            break

    if size_list:
        return [size_list] + args_copy
    else:
        return args_copy

# ==============================================
# = overwrite translate, rotate, scale, mirror =
# ==============================================
"""
    This block overwrites translate, scale, mirror and rotate from builtins
    to allow "overloading" those functions.
    As result you don't need to pass vectors in as lists, you can provide
    them as single integers / floats.

    translate([1, 2, 3])  ->   translate(1, 2, 3)
    rotate([1, 2, 3])   -> rotate(1, 2, 3)
"""

def translate(*args, **kwargs):
    args = extract_size_list(3, *args)
    return builtins.translate(*args, **kwargs)

def scale(*args, **kwargs):
    args = extract_size_list(3, *args)
    return builtins.scale(*args, **kwargs)

def resize(*args, **kwargs):
    args = extract_size_list(3, *args)
    return builtins.resize(*args, **kwargs)

def mirror(*args, **kwargs):
    args = extract_size_list(3, *args)
    return builtins.mirror(*args, **kwargs)

def rotate(*args, **kwargs):
    args = extract_size_list(3, *args)
    return builtins.rotate(*args, **kwargs)

def square(*args, **kwargs):
    args = extract_size_list(2, *args)
    return builtins.square(*args, **kwargs)

def cube(*args, **kwargs):
    args = extract_size_list(3, *args)
    return builtins.cube(*args, **kwargs)

# ==============
# = Directions =
# ==============
def up(z): return builtins.translate((0, 0, z))
def down(z): return builtins.translate((0, 0, -z))
def right(x): return builtins.translate((x, 0, 0))
def left(x): return builtins.translate((-x, 0, 0))
def forward(y): return builtins.translate((0, y, 0))
def fwd(y): return forward(y)
def back(y): return builtins.translate((0, -y, 0))

def translateX(x) : return builtins.translate((x, 0, 0))
def translateY(y) : return builtins.translate((0, y, 0))
def translateZ(z) : return builtins.translate((0, 0, z))

def rotateX(x): return rotate(x, 0, 0)
def rotateY(y): return rotate(0, y, 0)
def rotateZ(z): return rotate(0, 0, z)

def mirrorX(): return mirror(1, 0, 0)
def mirrorY(): return mirror(0, 1, 0)
def mirrorZ(): return mirror(0, 0, 1)

def scaleX(x): return scale(x, 0, 0)
def scaleY(y): return scale(0, y, 0)
def scaleZ(z): return scale(0, 0, z)

def resizeX(x): return resize(x, 0, 0)
def resizeY(y): return resize(0, y, 0)
def resizeZ(z): return resize(0, 0, z)

