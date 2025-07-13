from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/walls.scad'}", False)

class _bevelSolid(_Bosl2Base):
    def __init__(self, shape=None, bevel=None, **kwargs):
       super().__init__("_bevelSolid", {"shape" : shape, "bevel" : bevel, **kwargs})

class sparse_wall(_Bosl2Base):
    def __init__(self, h=None, l=None, thick=None, maxang=None, strut=None, max_bridge=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sparse_wall", {"h" : h, "l" : l, "thick" : thick, "maxang" : maxang, "strut" : strut, "max_bridge" : max_bridge, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sparse_wall2d(_Bosl2Base):
    def __init__(self, size=None, maxang=None, strut=None, max_bridge=None, anchor=None, spin=None, **kwargs):
       super().__init__("sparse_wall2d", {"size" : size, "maxang" : maxang, "strut" : strut, "max_bridge" : max_bridge, "anchor" : anchor, "spin" : spin, **kwargs})

class sparse_cuboid(_Bosl2Base):
    def __init__(self, size=None, dir=None, strut=None, maxang=None, max_bridge=None, chamfer=None, rounding=None, edges=None, _except=None, except_edges=None, trimcorners=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sparse_cuboid", {"size" : size, "dir" : dir, "strut" : strut, "maxang" : maxang, "max_bridge" : max_bridge, "chamfer" : chamfer, "rounding" : rounding, "edges" : edges, "_except" : _except, "except_edges" : except_edges, "trimcorners" : trimcorners, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class hex_panel(_Bosl2Base):
    def __init__(self, shape=None, strut=None, spacing=None, frame=None, bevel_frame=None, h=None, height=None, l=None, length=None, bevel=None, anchor=None, orient=None, cp=None, atype=None, spin=None, **kwargs):
       super().__init__("hex_panel", {"shape" : shape, "strut" : strut, "spacing" : spacing, "frame" : frame, "bevel_frame" : bevel_frame, "h" : h, "height" : height, "l" : l, "length" : length, "bevel" : bevel, "anchor" : anchor, "orient" : orient, "cp" : cp, "atype" : atype, "spin" : spin, **kwargs})

class _honeycomb(_Bosl2Base):
    def __init__(self, shape=None, spacing=None, hex_wall=None, **kwargs):
       super().__init__("_honeycomb", {"shape" : shape, "spacing" : spacing, "hex_wall" : hex_wall, **kwargs})

class _bevelWall(_Bosl2Base):
    def __init__(self, shape=None, bevel=None, thickness=None, **kwargs):
       super().__init__("_bevelWall", {"shape" : shape, "bevel" : bevel, "thickness" : thickness, **kwargs})

class corrugated_wall(_Bosl2Base):
    def __init__(self, h=None, l=None, thick=None, strut=None, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("corrugated_wall", {"h" : h, "l" : l, "thick" : thick, "strut" : strut, "wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class thinning_wall(_Bosl2Base):
    def __init__(self, h=None, l=None, thick=None, ang=None, braces=None, strut=None, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("thinning_wall", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "braces" : braces, "strut" : strut, "wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class thinning_triangle(_Bosl2Base):
    def __init__(self, h=None, l=None, thick=None, ang=None, strut=None, wall=None, diagonly=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("thinning_triangle", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "strut" : strut, "wall" : wall, "diagonly" : diagonly, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class narrowing_strut(_Bosl2Base):
    def __init__(self, w=None, l=None, wall=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("narrowing_strut", {"w" : w, "l" : l, "wall" : wall, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

