from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/nurbs.scad'}", False)

class nurbs_curve(_Bosl2Base):
    def __init__(self, control=None, degree=None, splinesteps=None, u=None, mult=None, weights=None, type=None, knots=None, **kwargs):
       super().__init__("nurbs_curve", {"control" : control, "degree" : degree, "splinesteps" : splinesteps, "u" : u, "mult" : mult, "weights" : weights, "type" : type, "knots" : knots, **kwargs})

class _nurbs_pt(_Bosl2Base):
    def __init__(self, knot=None, control=None, u=None, r=None, p=None, k=None, **kwargs):
       super().__init__("_nurbs_pt", {"knot" : knot, "control" : control, "u" : u, "r" : r, "p" : p, "k" : k, **kwargs})

class _extend_knot_mult(_Bosl2Base):
    def __init__(self, mult=None, next=None, len=None, **kwargs):
       super().__init__("_extend_knot_mult", {"mult" : mult, "next" : next, "len" : len, **kwargs})

class _extend_knot_vector(_Bosl2Base):
    def __init__(self, knots=None, next=None, len=None, **kwargs):
       super().__init__("_extend_knot_vector", {"knots" : knots, "next" : next, "len" : len, **kwargs})

class _calc_mult(_Bosl2Base):
    def __init__(self, knots=None, **kwargs):
       super().__init__("_calc_mult", {"knots" : knots, **kwargs})

class is_nurbs_patch(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_nurbs_patch", {"x" : x, **kwargs})

class nurbs_patch_points(_Bosl2Base):
    def __init__(self, patch=None, degree=None, splinesteps=None, u=None, v=None, weights=None, type=None, mult=None, knots=None, **kwargs):
       super().__init__("nurbs_patch_points", {"patch" : patch, "degree" : degree, "splinesteps" : splinesteps, "u" : u, "v" : v, "weights" : weights, "type" : type, "mult" : mult, "knots" : knots, **kwargs})

class nurbs_vnf(_Bosl2Base):
    def __init__(self, patch=None, degree=None, splinesteps=None, weights=None, type=None, mult=None, knots=None, style=None, **kwargs):
       super().__init__("nurbs_vnf", {"patch" : patch, "degree" : degree, "splinesteps" : splinesteps, "weights" : weights, "type" : type, "mult" : mult, "knots" : knots, "style" : style, **kwargs})

class debug_nurbs(_Bosl2Base):
    def __init__(self, control=None, degree=None, splinesteps=None, width=None, size=None, mult=None, weights=None, type=None, knots=None, show_weights=None, show_knots=None, show_index=None, **kwargs):
       super().__init__("debug_nurbs", {"control" : control, "degree" : degree, "splinesteps" : splinesteps, "width" : width, "size" : size, "mult" : mult, "weights" : weights, "type" : type, "knots" : knots, "show_weights" : show_weights, "show_knots" : show_knots, "show_index" : show_index, **kwargs})

