from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/hinges.scad'}", False)

class knuckle_hinge(_Bosl2Base):
    def __init__(self, length=None, segs=None, offset=None, inner=None, arm_height=None, arm_angle=None, gap=None, seg_ratio=None, knuckle_diam=None, pin_diam=None, fill=None, clear_top=None, round_bot=None, round_top=None, pin_fn=None, clearance=None, in_place=None, clip=None, tap_depth=None, screw_head=None, screw_tolerance=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("knuckle_hinge", {"length" : length, "segs" : segs, "offset" : offset, "inner" : inner, "arm_height" : arm_height, "arm_angle" : arm_angle, "gap" : gap, "seg_ratio" : seg_ratio, "knuckle_diam" : knuckle_diam, "pin_diam" : pin_diam, "fill" : fill, "clear_top" : clear_top, "round_bot" : round_bot, "round_top" : round_top, "pin_fn" : pin_fn, "clearance" : clearance, "in_place" : in_place, "clip" : clip, "tap_depth" : tap_depth, "screw_head" : screw_head, "screw_tolerance" : screw_tolerance, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})

class knuckle_hinge(_Bosl2Base):
    def __init__(self, length=None, segs=None, offset=None, inner=None, arm_height=None, arm_angle=None, gap=None, seg_ratio=None, knuckle_diam=None, pin_diam=None, fill=None, clear_top=None, round_bot=None, round_top=None, pin_fn=None, clearance=None, teardrop=None, in_place=None, clip=None, tap_depth=None, screw_head=None, screw_tolerance=None, knuckle_clearance=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("knuckle_hinge", {"length" : length, "segs" : segs, "offset" : offset, "inner" : inner, "arm_height" : arm_height, "arm_angle" : arm_angle, "gap" : gap, "seg_ratio" : seg_ratio, "knuckle_diam" : knuckle_diam, "pin_diam" : pin_diam, "fill" : fill, "clear_top" : clear_top, "round_bot" : round_bot, "round_top" : round_top, "pin_fn" : pin_fn, "clearance" : clearance, "teardrop" : teardrop, "in_place" : in_place, "clip" : clip, "tap_depth" : tap_depth, "screw_head" : screw_head, "screw_tolerance" : screw_tolerance, "knuckle_clearance" : knuckle_clearance, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})

class _knuckle_hinge_profile(_Bosl2Base):
    def __init__(self, offset=None, arm_height=None, arm_angle=None, knuckle_diam=None, pin_diam=None, fill=None, clear_top=None, round_bot=None, round_top=None, pin_fn=None, clearance=None, tearspin=None, clip=None, **kwargs):
       super().__init__("_knuckle_hinge_profile", {"offset" : offset, "arm_height" : arm_height, "arm_angle" : arm_angle, "knuckle_diam" : knuckle_diam, "pin_diam" : pin_diam, "fill" : fill, "clear_top" : clear_top, "round_bot" : round_bot, "round_top" : round_top, "pin_fn" : pin_fn, "clearance" : clearance, "tearspin" : tearspin, "clip" : clip, **kwargs})

class living_hinge_mask(_Bosl2Base):
    def __init__(self, l=None, thick=None, layerheight=None, foldangle=None, hingegap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("living_hinge_mask", {"l" : l, "thick" : thick, "layerheight" : layerheight, "foldangle" : foldangle, "hingegap" : hingegap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class folding_hinge_mask(_Bosl2Base):
    def __init__(self, l=None, thick=None, layerheight=None, foldangle=None, hingegap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("folding_hinge_mask", {"l" : l, "thick" : thick, "layerheight" : layerheight, "foldangle" : foldangle, "hingegap" : hingegap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class apply_folding_hinges_and_snaps(_Bosl2Base):
    def __init__(self, thick=None, foldangle=None, hinges=None, snaps=None, sockets=None, snaplen=None, snapdiam=None, hingegap=None, layerheight=None, **kwargs):
       super().__init__("apply_folding_hinges_and_snaps", {"thick" : thick, "foldangle" : foldangle, "hinges" : hinges, "snaps" : snaps, "sockets" : sockets, "snaplen" : snaplen, "snapdiam" : snapdiam, "hingegap" : hingegap, "layerheight" : layerheight, **kwargs})

class snap_lock(_Bosl2Base):
    def __init__(self, thick=None, snaplen=None, snapdiam=None, layerheight=None, foldangle=None, hingegap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("snap_lock", {"thick" : thick, "snaplen" : snaplen, "snapdiam" : snapdiam, "layerheight" : layerheight, "foldangle" : foldangle, "hingegap" : hingegap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class snap_socket(_Bosl2Base):
    def __init__(self, thick=None, snaplen=None, snapdiam=None, layerheight=None, foldangle=None, hingegap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("snap_socket", {"thick" : thick, "snaplen" : snaplen, "snapdiam" : snapdiam, "layerheight" : layerheight, "foldangle" : foldangle, "hingegap" : hingegap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

