from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/masks3d.scad'}", False)

class chamfer_edge_mask(_Bosl2Base):
    def __init__(self, l=None, chamfer=None, excess=None, h=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("chamfer_edge_mask", {"l" : l, "chamfer" : chamfer, "excess" : excess, "h" : h, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class chamfer_corner_mask(_Bosl2Base):
    def __init__(self, chamfer=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("chamfer_corner_mask", {"chamfer" : chamfer, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class chamfer_cylinder_mask(_Bosl2Base):
    def __init__(self, r=None, chamfer=None, d=None, ang=None, from_end=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("chamfer_cylinder_mask", {"r" : r, "chamfer" : chamfer, "d" : d, "ang" : ang, "from_end" : from_end, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_edge_mask(_Bosl2Base):
    def __init__(self, l=None, r=None, ang=None, r1=None, r2=None, d=None, d1=None, d2=None, excess=None, anchor=None, spin=None, orient=None, h=None, height=None, length=None, **kwargs):
       super().__init__("rounding_edge_mask", {"l" : l, "r" : r, "ang" : ang, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "excess" : excess, "anchor" : anchor, "spin" : spin, "orient" : orient, "h" : h, "height" : height, "length" : length, **kwargs})

class rounding_corner_mask(_Bosl2Base):
    def __init__(self, r=None, ang=None, d=None, style=None, excess=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_corner_mask", {"r" : r, "ang" : ang, "d" : d, "style" : style, "excess" : excess, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_angled_edge_mask(_Bosl2Base):
    def __init__(self, h=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, ang=None, anchor=None, spin=None, orient=None, l=None, height=None, length=None, **kwargs):
       super().__init__("rounding_angled_edge_mask", {"h" : h, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, "height" : height, "length" : length, **kwargs})

class rounding_angled_corner_mask(_Bosl2Base):
    def __init__(self, r=None, ang=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_angled_corner_mask", {"r" : r, "ang" : ang, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_cylinder_mask(_Bosl2Base):
    def __init__(self, r=None, rounding=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_cylinder_mask", {"r" : r, "rounding" : rounding, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_hole_mask(_Bosl2Base):
    def __init__(self, r=None, rounding=None, excess=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_hole_mask", {"r" : r, "rounding" : rounding, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class teardrop_edge_mask(_Bosl2Base):
    def __init__(self, l=None, r=None, angle=None, excess=None, d=None, anchor=None, spin=None, orient=None, h=None, height=None, length=None, **kwargs):
       super().__init__("teardrop_edge_mask", {"l" : l, "r" : r, "angle" : angle, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, "h" : h, "height" : height, "length" : length, **kwargs})

class teardrop_corner_mask(_Bosl2Base):
    def __init__(self, r=None, angle=None, excess=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("teardrop_corner_mask", {"r" : r, "angle" : angle, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class chamfer_edge_mask(_Bosl2Base):
    def __init__(self, l=None, chamfer=None, excess=None, h=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("chamfer_edge_mask", {"l" : l, "chamfer" : chamfer, "excess" : excess, "h" : h, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class chamfer_corner_mask(_Bosl2Base):
    def __init__(self, chamfer=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("chamfer_corner_mask", {"chamfer" : chamfer, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class chamfer_cylinder_mask(_Bosl2Base):
    def __init__(self, r=None, chamfer=None, d=None, ang=None, from_end=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("chamfer_cylinder_mask", {"r" : r, "chamfer" : chamfer, "d" : d, "ang" : ang, "from_end" : from_end, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_edge_mask(_Bosl2Base):
    def __init__(self, l=None, r=None, ang=None, r1=None, r2=None, excess=None, d1=None, d2=None, d=None, length=None, h=None, height=None, anchor=None, spin=None, orient=None, rounding=None, rounding1=None, rounding2=None, chamfer=None, chamfer1=None, chamfer2=None, _remove_tag=None, **kwargs):
       super().__init__("rounding_edge_mask", {"l" : l, "r" : r, "ang" : ang, "r1" : r1, "r2" : r2, "excess" : excess, "d1" : d1, "d2" : d2, "d" : d, "length" : length, "h" : h, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "_remove_tag" : _remove_tag, **kwargs})

class rounding_corner_mask(_Bosl2Base):
    def __init__(self, r=None, ang=None, d=None, style=None, excess=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_corner_mask", {"r" : r, "ang" : ang, "d" : d, "style" : style, "excess" : excess, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_angled_edge_mask(_Bosl2Base):
    def __init__(self, h=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, ang=None, anchor=None, spin=None, orient=None, l=None, height=None, length=None, **kwargs):
       super().__init__("rounding_angled_edge_mask", {"h" : h, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, "height" : height, "length" : length, **kwargs})

class rounding_angled_corner_mask(_Bosl2Base):
    def __init__(self, r=None, ang=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_angled_corner_mask", {"r" : r, "ang" : ang, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_cylinder_mask(_Bosl2Base):
    def __init__(self, r=None, rounding=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_cylinder_mask", {"r" : r, "rounding" : rounding, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rounding_hole_mask(_Bosl2Base):
    def __init__(self, r=None, rounding=None, excess=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rounding_hole_mask", {"r" : r, "rounding" : rounding, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class teardrop_edge_mask(_Bosl2Base):
    def __init__(self, l=None, r=None, angle=None, excess=None, d=None, anchor=None, spin=None, orient=None, h=None, height=None, length=None, **kwargs):
       super().__init__("teardrop_edge_mask", {"l" : l, "r" : r, "angle" : angle, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, "h" : h, "height" : height, "length" : length, **kwargs})

class teardrop_corner_mask(_Bosl2Base):
    def __init__(self, r=None, angle=None, excess=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("teardrop_corner_mask", {"r" : r, "angle" : angle, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

