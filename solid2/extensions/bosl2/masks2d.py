from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/masks2d.scad'}", False)

class _inset_corner(_Bosl2Base):
    def __init__(self, corner=None, mask_angle=None, inset=None, excess=None, flat_top=None, **kwargs):
       super().__init__("_inset_corner", {"corner" : corner, "mask_angle" : mask_angle, "inset" : inset, "excess" : excess, "flat_top" : flat_top, **kwargs})

class mask2d_roundover(_Bosl2Base):
    def __init__(self, r=None, inset=None, mask_angle=None, excess=None, clip_angle=None, flat_top=None, quarter_round=None, d=None, h=None, height=None, cut=None, joint=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_roundover", {"r" : r, "inset" : inset, "mask_angle" : mask_angle, "excess" : excess, "clip_angle" : clip_angle, "flat_top" : flat_top, "quarter_round" : quarter_round, "d" : d, "h" : h, "height" : height, "cut" : cut, "joint" : joint, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_teardrop(_Bosl2Base):
    def __init__(self, r=None, angle=None, inset=None, mask_angle=None, excess=None, flat_top=None, d=None, h=None, height=None, cut=None, joint=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_teardrop", {"r" : r, "angle" : angle, "inset" : inset, "mask_angle" : mask_angle, "excess" : excess, "flat_top" : flat_top, "d" : d, "h" : h, "height" : height, "cut" : cut, "joint" : joint, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_cove(_Bosl2Base):
    def __init__(self, r=None, inset=None, mask_angle=None, excess=None, flat_top=None, d=None, h=None, height=None, bulge=None, quarter_round=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_cove", {"r" : r, "inset" : inset, "mask_angle" : mask_angle, "excess" : excess, "flat_top" : flat_top, "d" : d, "h" : h, "height" : height, "bulge" : bulge, "quarter_round" : quarter_round, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_chamfer(_Bosl2Base):
    def __init__(self, edge=None, angle=None, inset=None, excess=None, mask_angle=None, flat_top=None, x=None, y=None, h=None, w=None, width=None, height=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_chamfer", {"edge" : edge, "angle" : angle, "inset" : inset, "excess" : excess, "mask_angle" : mask_angle, "flat_top" : flat_top, "x" : x, "y" : y, "h" : h, "w" : w, "width" : width, "height" : height, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_rabbet(_Bosl2Base):
    def __init__(self, size=None, mask_angle=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_rabbet", {"size" : size, "mask_angle" : mask_angle, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_dovetail(_Bosl2Base):
    def __init__(self, edge=None, angle=None, slope=None, shelf=None, inset=None, mask_angle=None, excess=None, flat_top=None, w=None, width=None, h=None, height=None, anchor=None, spin=None, x=None, y=None, **kwargs):
       super().__init__("mask2d_dovetail", {"edge" : edge, "angle" : angle, "slope" : slope, "shelf" : shelf, "inset" : inset, "mask_angle" : mask_angle, "excess" : excess, "flat_top" : flat_top, "w" : w, "width" : width, "h" : h, "height" : height, "anchor" : anchor, "spin" : spin, "x" : x, "y" : y, **kwargs})

class mask2d_ogee(_Bosl2Base):
    def __init__(self, pattern=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_ogee", {"pattern" : pattern, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_roundover(_Bosl2Base):
    def __init__(self, r=None, inset=None, mask_angle=None, excess=None, flat_top=None, d=None, h=None, height=None, cut=None, quarter_round=None, joint=None, anchor=None, spin=None, clip_angle=None, **kwargs):
       super().__init__("mask2d_roundover", {"r" : r, "inset" : inset, "mask_angle" : mask_angle, "excess" : excess, "flat_top" : flat_top, "d" : d, "h" : h, "height" : height, "cut" : cut, "quarter_round" : quarter_round, "joint" : joint, "anchor" : anchor, "spin" : spin, "clip_angle" : clip_angle, **kwargs})

class mask2d_teardrop(_Bosl2Base):
    def __init__(self, r=None, angle=None, mask_angle=None, excess=None, inset=None, flat_top=None, height=None, d=None, h=None, cut=None, joint=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_teardrop", {"r" : r, "angle" : angle, "mask_angle" : mask_angle, "excess" : excess, "inset" : inset, "flat_top" : flat_top, "height" : height, "d" : d, "h" : h, "cut" : cut, "joint" : joint, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_cove(_Bosl2Base):
    def __init__(self, r=None, inset=None, mask_angle=None, excess=None, flat_top=None, bulge=None, d=None, h=None, height=None, quarter_round=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_cove", {"r" : r, "inset" : inset, "mask_angle" : mask_angle, "excess" : excess, "flat_top" : flat_top, "bulge" : bulge, "d" : d, "h" : h, "height" : height, "quarter_round" : quarter_round, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_chamfer(_Bosl2Base):
    def __init__(self, edge=None, angle=None, inset=None, excess=None, mask_angle=None, flat_top=None, x=None, y=None, h=None, w=None, height=None, width=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_chamfer", {"edge" : edge, "angle" : angle, "inset" : inset, "excess" : excess, "mask_angle" : mask_angle, "flat_top" : flat_top, "x" : x, "y" : y, "h" : h, "w" : w, "height" : height, "width" : width, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_rabbet(_Bosl2Base):
    def __init__(self, size=None, mask_angle=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_rabbet", {"size" : size, "mask_angle" : mask_angle, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_dovetail(_Bosl2Base):
    def __init__(self, edge=None, angle=None, shelf=None, inset=None, mask_angle=None, excess=None, flat_top=None, w=None, h=None, width=None, height=None, slope=None, anchor=None, spin=None, x=None, y=None, **kwargs):
       super().__init__("mask2d_dovetail", {"edge" : edge, "angle" : angle, "shelf" : shelf, "inset" : inset, "mask_angle" : mask_angle, "excess" : excess, "flat_top" : flat_top, "w" : w, "h" : h, "width" : width, "height" : height, "slope" : slope, "anchor" : anchor, "spin" : spin, "x" : x, "y" : y, **kwargs})

class mask2d_ogee(_Bosl2Base):
    def __init__(self, pattern=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_ogee", {"pattern" : pattern, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

