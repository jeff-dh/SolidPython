from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/transforms.scad'}", False)

_NO_ARG = _OpenSCADConstant('_NO_ARG')
_transform = _OpenSCADConstant('_transform')
class move(_Bosl2Base):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("move", {"v" : v, "p" : p, **kwargs})

class translate(_Bosl2Base):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("translate", {"v" : v, "p" : p, **kwargs})

class left(_Bosl2Base):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("left", {"x" : x, "p" : p, **kwargs})

class right(_Bosl2Base):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("right", {"x" : x, "p" : p, **kwargs})

class xmove(_Bosl2Base):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("xmove", {"x" : x, "p" : p, **kwargs})

class fwd(_Bosl2Base):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("fwd", {"y" : y, "p" : p, **kwargs})

class back(_Bosl2Base):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("back", {"y" : y, "p" : p, **kwargs})

class ymove(_Bosl2Base):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("ymove", {"y" : y, "p" : p, **kwargs})

class down(_Bosl2Base):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("down", {"z" : z, "p" : p, **kwargs})

class up(_Bosl2Base):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("up", {"z" : z, "p" : p, **kwargs})

class zmove(_Bosl2Base):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("zmove", {"z" : z, "p" : p, **kwargs})

class rot(_Bosl2Base):
    def __init__(self, a=None, v=None, cp=None, _from=None, to=None, reverse=None, p=None, **kwargs):
       super().__init__("rot", {"a" : a, "v" : v, "cp" : cp, "_from" : _from, "to" : to, "reverse" : reverse, "p" : p, **kwargs})

class xrot(_Bosl2Base):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("xrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class yrot(_Bosl2Base):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("yrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class zrot(_Bosl2Base):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("zrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class tilt(_Bosl2Base):
    def __init__(self, to=None, cp=None, reverse=None, p=None, **kwargs):
       super().__init__("tilt", {"to" : to, "cp" : cp, "reverse" : reverse, "p" : p, **kwargs})

class scale(_Bosl2Base):
    def __init__(self, v=None, p=None, cp=None, **kwargs):
       super().__init__("scale", {"v" : v, "p" : p, "cp" : cp, **kwargs})

class xscale(_Bosl2Base):
    def __init__(self, x=None, p=None, cp=None, **kwargs):
       super().__init__("xscale", {"x" : x, "p" : p, "cp" : cp, **kwargs})

class yscale(_Bosl2Base):
    def __init__(self, y=None, p=None, cp=None, **kwargs):
       super().__init__("yscale", {"y" : y, "p" : p, "cp" : cp, **kwargs})

class zscale(_Bosl2Base):
    def __init__(self, z=None, p=None, cp=None, **kwargs):
       super().__init__("zscale", {"z" : z, "p" : p, "cp" : cp, **kwargs})

class mirror(_Bosl2Base):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("mirror", {"v" : v, "p" : p, **kwargs})

class xflip(_Bosl2Base):
    def __init__(self, p=None, x=None, **kwargs):
       super().__init__("xflip", {"p" : p, "x" : x, **kwargs})

class yflip(_Bosl2Base):
    def __init__(self, p=None, y=None, **kwargs):
       super().__init__("yflip", {"p" : p, "y" : y, **kwargs})

class zflip(_Bosl2Base):
    def __init__(self, p=None, z=None, **kwargs):
       super().__init__("zflip", {"p" : p, "z" : z, **kwargs})

class frame_map(_Bosl2Base):
    def __init__(self, x=None, y=None, z=None, p=None, reverse=None, **kwargs):
       super().__init__("frame_map", {"x" : x, "y" : y, "z" : z, "p" : p, "reverse" : reverse, **kwargs})

class skew(_Bosl2Base):
    def __init__(self, p=None, sxy=None, sxz=None, syx=None, syz=None, szx=None, szy=None, axy=None, axz=None, ayx=None, ayz=None, azx=None, azy=None, **kwargs):
       super().__init__("skew", {"p" : p, "sxy" : sxy, "sxz" : sxz, "syx" : syx, "syz" : syz, "szx" : szx, "szy" : szy, "axy" : axy, "axz" : axz, "ayx" : ayx, "ayz" : ayz, "azx" : azx, "azy" : azy, **kwargs})

class is_2d_transform(_Bosl2Base):
    def __init__(self, t=None, **kwargs):
       super().__init__("is_2d_transform", {"t" : t, **kwargs})

class apply(_Bosl2Base):
    def __init__(self, transform=None, points=None, **kwargs):
       super().__init__("apply", {"transform" : transform, "points" : points, **kwargs})

class _apply(_Bosl2Base):
    def __init__(self, transform=None, points=None, **kwargs):
       super().__init__("_apply", {"transform" : transform, "points" : points, **kwargs})

class move(_Bosl2Base):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("move", {"v" : v, "p" : p, **kwargs})

class left(_Bosl2Base):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("left", {"x" : x, "p" : p, **kwargs})

class right(_Bosl2Base):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("right", {"x" : x, "p" : p, **kwargs})

class xmove(_Bosl2Base):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("xmove", {"x" : x, "p" : p, **kwargs})

class fwd(_Bosl2Base):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("fwd", {"y" : y, "p" : p, **kwargs})

class back(_Bosl2Base):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("back", {"y" : y, "p" : p, **kwargs})

class ymove(_Bosl2Base):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("ymove", {"y" : y, "p" : p, **kwargs})

class down(_Bosl2Base):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("down", {"z" : z, "p" : p, **kwargs})

class up(_Bosl2Base):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("up", {"z" : z, "p" : p, **kwargs})

class zmove(_Bosl2Base):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("zmove", {"z" : z, "p" : p, **kwargs})

class rot(_Bosl2Base):
    def __init__(self, a=None, v=None, cp=None, _from=None, to=None, reverse=None, **kwargs):
       super().__init__("rot", {"a" : a, "v" : v, "cp" : cp, "_from" : _from, "to" : to, "reverse" : reverse, **kwargs})

class xrot(_Bosl2Base):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("xrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class yrot(_Bosl2Base):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("yrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class zrot(_Bosl2Base):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("zrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class tilt(_Bosl2Base):
    def __init__(self, to=None, cp=None, reverse=None, **kwargs):
       super().__init__("tilt", {"to" : to, "cp" : cp, "reverse" : reverse, **kwargs})

class xscale(_Bosl2Base):
    def __init__(self, x=None, p=None, cp=None, **kwargs):
       super().__init__("xscale", {"x" : x, "p" : p, "cp" : cp, **kwargs})

class yscale(_Bosl2Base):
    def __init__(self, y=None, p=None, cp=None, **kwargs):
       super().__init__("yscale", {"y" : y, "p" : p, "cp" : cp, **kwargs})

class zscale(_Bosl2Base):
    def __init__(self, z=None, p=None, cp=None, **kwargs):
       super().__init__("zscale", {"z" : z, "p" : p, "cp" : cp, **kwargs})

class xflip(_Bosl2Base):
    def __init__(self, p=None, x=None, **kwargs):
       super().__init__("xflip", {"p" : p, "x" : x, **kwargs})

class yflip(_Bosl2Base):
    def __init__(self, p=None, y=None, **kwargs):
       super().__init__("yflip", {"p" : p, "y" : y, **kwargs})

class zflip(_Bosl2Base):
    def __init__(self, p=None, z=None, **kwargs):
       super().__init__("zflip", {"p" : p, "z" : z, **kwargs})

class frame_map(_Bosl2Base):
    def __init__(self, x=None, y=None, z=None, p=None, reverse=None, **kwargs):
       super().__init__("frame_map", {"x" : x, "y" : y, "z" : z, "p" : p, "reverse" : reverse, **kwargs})

class skew(_Bosl2Base):
    def __init__(self, p=None, sxy=None, sxz=None, syx=None, syz=None, szx=None, szy=None, axy=None, axz=None, ayx=None, ayz=None, azx=None, azy=None, **kwargs):
       super().__init__("skew", {"p" : p, "sxy" : sxy, "sxz" : sxz, "syx" : syx, "syz" : syz, "szx" : szx, "szy" : szy, "axy" : axy, "axz" : axz, "ayx" : ayx, "ayz" : ayz, "azx" : azx, "azy" : azy, **kwargs})

class translate(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("translate", {"v" : v, **kwargs})

class rotate(_Bosl2Base):
    def __init__(self, a=None, v=None, **kwargs):
       super().__init__("rotate", {"a" : a, "v" : v, **kwargs})

class scale(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("scale", {"v" : v, **kwargs})

class multmatrix(_Bosl2Base):
    def __init__(self, m=None, **kwargs):
       super().__init__("multmatrix", {"m" : m, **kwargs})

