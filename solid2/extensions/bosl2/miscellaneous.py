from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/miscellaneous.scad'}", False)

class extrude_from_to(_Bosl2Base):
    def __init__(self, pt1=None, pt2=None, convexity=None, twist=None, scale=None, slices=None, **kwargs):
       super().__init__("extrude_from_to", {"pt1" : pt1, "pt2" : pt2, "convexity" : convexity, "twist" : twist, "scale" : scale, "slices" : slices, **kwargs})

class path_extrude2d(_Bosl2Base):
    def __init__(self, path=None, caps=None, closed=None, s=None, convexity=None, **kwargs):
       super().__init__("path_extrude2d", {"path" : path, "caps" : caps, "closed" : closed, "s" : s, "convexity" : convexity, **kwargs})

class path_extrude(_Bosl2Base):
    def __init__(self, path=None, convexity=None, clipsize=None, **kwargs):
       super().__init__("path_extrude", {"path" : path, "convexity" : convexity, "clipsize" : clipsize, **kwargs})

class cylindrical_extrude(_Bosl2Base):
    def __init__(self, ir=None, _or=None, od=None, id=None, size=None, convexity=None, spin=None, orient=None, **kwargs):
       super().__init__("cylindrical_extrude", {"ir" : ir, "_or" : _or, "od" : od, "id" : id, "size" : size, "convexity" : convexity, "spin" : spin, "orient" : orient, **kwargs})

class bounding_box(_Bosl2Base):
    def __init__(self, excess=None, planar=None, **kwargs):
       super().__init__("bounding_box", {"excess" : excess, "planar" : planar, **kwargs})

class chain_hull(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("chain_hull", {**kwargs})

class minkowski_difference(_Bosl2Base):
    def __init__(self, planar=None, **kwargs):
       super().__init__("minkowski_difference", {"planar" : planar, **kwargs})

class offset3d(_Bosl2Base):
    def __init__(self, r=None, size=None, convexity=None, **kwargs):
       super().__init__("offset3d", {"r" : r, "size" : size, "convexity" : convexity, **kwargs})

class round3d(_Bosl2Base):
    def __init__(self, r=None, _or=None, ir=None, size=None, **kwargs):
       super().__init__("round3d", {"r" : r, "_or" : _or, "ir" : ir, "size" : size, **kwargs})

