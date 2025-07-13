from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/gears.scad'}", False)

_GEAR_PITCH = _OpenSCADConstant('_GEAR_PITCH')
_GEAR_HELICAL = _OpenSCADConstant('_GEAR_HELICAL')
_GEAR_THICKNESS = _OpenSCADConstant('_GEAR_THICKNESS')
_GEAR_PA = _OpenSCADConstant('_GEAR_PA')
_parent_gear_type = _OpenSCADConstant('_parent_gear_type')
_parent_gear_pitch = _OpenSCADConstant('_parent_gear_pitch')
_parent_gear_teeth = _OpenSCADConstant('_parent_gear_teeth')
_parent_gear_pa = _OpenSCADConstant('_parent_gear_pa')
_parent_gear_helical = _OpenSCADConstant('_parent_gear_helical')
_parent_gear_thickness = _OpenSCADConstant('_parent_gear_thickness')
_parent_gear_dir = _OpenSCADConstant('_parent_gear_dir')
_parent_gear_travel = _OpenSCADConstant('_parent_gear_travel')
class _inherit_gear_param(_Bosl2Base):
    def __init__(self, name=None, val=None, pval=None, dflt=None, invert=None, **kwargs):
       super().__init__("_inherit_gear_param", {"name" : name, "val" : val, "pval" : pval, "dflt" : dflt, "invert" : invert, **kwargs})

class _inherit_gear_pitch(_Bosl2Base):
    def __init__(self, fname=None, pitch=None, circ_pitch=None, diam_pitch=None, mod=None, warn=None, **kwargs):
       super().__init__("_inherit_gear_pitch", {"fname" : fname, "pitch" : pitch, "circ_pitch" : circ_pitch, "diam_pitch" : diam_pitch, "mod" : mod, "warn" : warn, **kwargs})

class _inherit_gear_pa(_Bosl2Base):
    def __init__(self, pressure_angle=None, **kwargs):
       super().__init__("_inherit_gear_pa", {"pressure_angle" : pressure_angle, **kwargs})

class _inherit_gear_helical(_Bosl2Base):
    def __init__(self, helical=None, invert=None, **kwargs):
       super().__init__("_inherit_gear_helical", {"helical" : helical, "invert" : invert, **kwargs})

class _inherit_gear_thickness(_Bosl2Base):
    def __init__(self, thickness=None, dflt=None, **kwargs):
       super().__init__("_inherit_gear_thickness", {"thickness" : thickness, "dflt" : dflt, **kwargs})

class spur_gear(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, thickness=None, shaft_diam=None, hide=None, pressure_angle=None, clearance=None, backlash=None, helical=None, interior=None, internal=None, profile_shift=None, slices=None, herringbone=None, shorten=None, diam_pitch=None, mod=None, pitch=None, gear_spin=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spur_gear", {"circ_pitch" : circ_pitch, "teeth" : teeth, "thickness" : thickness, "shaft_diam" : shaft_diam, "hide" : hide, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "helical" : helical, "interior" : interior, "internal" : internal, "profile_shift" : profile_shift, "slices" : slices, "herringbone" : herringbone, "shorten" : shorten, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, "gear_spin" : gear_spin, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class spur_gear2d(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, hide=None, pressure_angle=None, clearance=None, backlash=None, internal=None, interior=None, profile_shift=None, helical=None, shaft_diam=None, shorten=None, pitch=None, diam_pitch=None, mod=None, gear_spin=None, atype=None, anchor=None, spin=None, **kwargs):
       super().__init__("spur_gear2d", {"circ_pitch" : circ_pitch, "teeth" : teeth, "hide" : hide, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "internal" : internal, "interior" : interior, "profile_shift" : profile_shift, "helical" : helical, "shaft_diam" : shaft_diam, "shorten" : shorten, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "gear_spin" : gear_spin, "atype" : atype, "anchor" : anchor, "spin" : spin, **kwargs})

class rack(_Bosl2Base):
    def __init__(self, pitch=None, teeth=None, thickness=None, backing=None, bottom=None, width=None, pressure_angle=None, backlash=None, clearance=None, helical=None, herringbone=None, profile_shift=None, circ_pitch=None, diam_pitch=None, mod=None, gear_travel=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rack", {"pitch" : pitch, "teeth" : teeth, "thickness" : thickness, "backing" : backing, "bottom" : bottom, "width" : width, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "helical" : helical, "herringbone" : herringbone, "profile_shift" : profile_shift, "circ_pitch" : circ_pitch, "diam_pitch" : diam_pitch, "mod" : mod, "gear_travel" : gear_travel, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rack2d(_Bosl2Base):
    def __init__(self, pitch=None, teeth=None, backing=None, pressure_angle=None, backlash=None, clearance=None, helical=None, profile_shift=None, circ_pitch=None, diam_pitch=None, mod=None, width=None, bottom=None, gear_travel=None, rounding=None, anchor=None, spin=None, **kwargs):
       super().__init__("rack2d", {"pitch" : pitch, "teeth" : teeth, "backing" : backing, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "helical" : helical, "profile_shift" : profile_shift, "circ_pitch" : circ_pitch, "diam_pitch" : diam_pitch, "mod" : mod, "width" : width, "bottom" : bottom, "gear_travel" : gear_travel, "rounding" : rounding, "anchor" : anchor, "spin" : spin, **kwargs})

class crown_gear(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, backing=None, face_width=None, pressure_angle=None, clearance=None, backlash=None, profile_shift=None, slices=None, bottom=None, thickness=None, diam_pitch=None, pitch=None, mod=None, gear_spin=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("crown_gear", {"circ_pitch" : circ_pitch, "teeth" : teeth, "backing" : backing, "face_width" : face_width, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "profile_shift" : profile_shift, "slices" : slices, "bottom" : bottom, "thickness" : thickness, "diam_pitch" : diam_pitch, "pitch" : pitch, "mod" : mod, "gear_spin" : gear_spin, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class bevel_gear(_Bosl2Base):
    def __init__(self, teeth=None, mate_teeth=None, shaft_angle=None, backing=None, thickness=None, bottom=None, face_width=None, pressure_angle=None, clearance=None, backlash=None, cutter_radius=None, spiral=None, right_handed=None, slices=None, cone_backing=None, pitch=None, circ_pitch=None, diam_pitch=None, mod=None, anchor=None, spin=None, gear_spin=None, orient=None, _return_anchors=None, **kwargs):
       super().__init__("bevel_gear", {"teeth" : teeth, "mate_teeth" : mate_teeth, "shaft_angle" : shaft_angle, "backing" : backing, "thickness" : thickness, "bottom" : bottom, "face_width" : face_width, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "cutter_radius" : cutter_radius, "spiral" : spiral, "right_handed" : right_handed, "slices" : slices, "cone_backing" : cone_backing, "pitch" : pitch, "circ_pitch" : circ_pitch, "diam_pitch" : diam_pitch, "mod" : mod, "anchor" : anchor, "spin" : spin, "gear_spin" : gear_spin, "orient" : orient, "_return_anchors" : _return_anchors, **kwargs})

class worm(_Bosl2Base):
    def __init__(self, circ_pitch=None, d=None, l=None, starts=None, left_handed=None, pressure_angle=None, backlash=None, clearance=None, diam_pitch=None, mod=None, pitch=None, gear_spin=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("worm", {"circ_pitch" : circ_pitch, "d" : d, "l" : l, "starts" : starts, "left_handed" : left_handed, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, "gear_spin" : gear_spin, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class enveloping_worm(_Bosl2Base):
    def __init__(self, circ_pitch=None, mate_teeth=None, d=None, left_handed=None, starts=None, arc=None, pressure_angle=None, gear_spin=None, rounding=None, taper=None, diam_pitch=None, mod=None, pitch=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("enveloping_worm", {"circ_pitch" : circ_pitch, "mate_teeth" : mate_teeth, "d" : d, "left_handed" : left_handed, "starts" : starts, "arc" : arc, "pressure_angle" : pressure_angle, "gear_spin" : gear_spin, "rounding" : rounding, "taper" : taper, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class worm_gear(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, worm_diam=None, worm_starts=None, worm_arc=None, crowning=None, left_handed=None, pressure_angle=None, backlash=None, clearance=None, profile_shift=None, slices=None, gear_spin=None, pitch=None, diam_pitch=None, mod=None, get_thickness=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("worm_gear", {"circ_pitch" : circ_pitch, "teeth" : teeth, "worm_diam" : worm_diam, "worm_starts" : worm_starts, "worm_arc" : worm_arc, "crowning" : crowning, "left_handed" : left_handed, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "profile_shift" : profile_shift, "slices" : slices, "gear_spin" : gear_spin, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "get_thickness" : get_thickness, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _gear_tooth_profile(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, pressure_angle=None, clearance=None, backlash=None, helical=None, internal=None, profile_shift=None, shorten=None, mod=None, diam_pitch=None, pitch=None, center=None, **kwargs):
       super().__init__("_gear_tooth_profile", {"circ_pitch" : circ_pitch, "teeth" : teeth, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "helical" : helical, "internal" : internal, "profile_shift" : profile_shift, "shorten" : shorten, "mod" : mod, "diam_pitch" : diam_pitch, "pitch" : pitch, "center" : center, **kwargs})

class planetary_gears(_Bosl2Base):
    def __init__(self, n=None, max_teeth=None, helical=None, circ_pitch=None, mod=None, diam_pitch=None, ring_carrier=None, carrier_ring=None, sun_carrier=None, carrier_sun=None, sun_ring=None, ring_sun=None, gear_spin=None, **kwargs):
       super().__init__("planetary_gears", {"n" : n, "max_teeth" : max_teeth, "helical" : helical, "circ_pitch" : circ_pitch, "mod" : mod, "diam_pitch" : diam_pitch, "ring_carrier" : ring_carrier, "carrier_ring" : carrier_ring, "sun_carrier" : sun_carrier, "carrier_sun" : carrier_sun, "sun_ring" : sun_ring, "ring_sun" : ring_sun, "gear_spin" : gear_spin, **kwargs})

class circular_pitch(_Bosl2Base):
    def __init__(self, circ_pitch=None, mod=None, pitch=None, diam_pitch=None, **kwargs):
       super().__init__("circular_pitch", {"circ_pitch" : circ_pitch, "mod" : mod, "pitch" : pitch, "diam_pitch" : diam_pitch, **kwargs})

class diametral_pitch(_Bosl2Base):
    def __init__(self, circ_pitch=None, mod=None, pitch=None, diam_pitch=None, **kwargs):
       super().__init__("diametral_pitch", {"circ_pitch" : circ_pitch, "mod" : mod, "pitch" : pitch, "diam_pitch" : diam_pitch, **kwargs})

class module_value(_Bosl2Base):
    def __init__(self, circ_pitch=None, mod=None, pitch=None, diam_pitch=None, **kwargs):
       super().__init__("module_value", {"circ_pitch" : circ_pitch, "mod" : mod, "pitch" : pitch, "diam_pitch" : diam_pitch, **kwargs})

class _adendum(_Bosl2Base):
    def __init__(self, circ_pitch=None, profile_shift=None, shorten=None, diam_pitch=None, mod=None, pitch=None, **kwargs):
       super().__init__("_adendum", {"circ_pitch" : circ_pitch, "profile_shift" : profile_shift, "shorten" : shorten, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, **kwargs})

class _dedendum(_Bosl2Base):
    def __init__(self, circ_pitch=None, clearance=None, profile_shift=None, diam_pitch=None, mod=None, pitch=None, **kwargs):
       super().__init__("_dedendum", {"circ_pitch" : circ_pitch, "clearance" : clearance, "profile_shift" : profile_shift, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, **kwargs})

class pitch_radius(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, helical=None, mod=None, diam_pitch=None, pitch=None, **kwargs):
       super().__init__("pitch_radius", {"circ_pitch" : circ_pitch, "teeth" : teeth, "helical" : helical, "mod" : mod, "diam_pitch" : diam_pitch, "pitch" : pitch, **kwargs})

class outer_radius(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, clearance=None, internal=None, helical=None, profile_shift=None, pressure_angle=None, shorten=None, mod=None, pitch=None, diam_pitch=None, **kwargs):
       super().__init__("outer_radius", {"circ_pitch" : circ_pitch, "teeth" : teeth, "clearance" : clearance, "internal" : internal, "helical" : helical, "profile_shift" : profile_shift, "pressure_angle" : pressure_angle, "shorten" : shorten, "mod" : mod, "pitch" : pitch, "diam_pitch" : diam_pitch, **kwargs})

class root_radius(_Bosl2Base):
    def __init__(self, teeth=None, helical=None, clearance=None, internal=None, profile_shift=None, pressure_angle=None, mod=None, pitch=None, diam_pitch=None, backlash=None, **kwargs):
       super().__init__("root_radius", {"teeth" : teeth, "helical" : helical, "clearance" : clearance, "internal" : internal, "profile_shift" : profile_shift, "pressure_angle" : pressure_angle, "mod" : mod, "pitch" : pitch, "diam_pitch" : diam_pitch, "backlash" : backlash, **kwargs})

class _root_radius_basic(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, clearance=None, internal=None, helical=None, profile_shift=None, diam_pitch=None, mod=None, pitch=None, **kwargs):
       super().__init__("_root_radius_basic", {"circ_pitch" : circ_pitch, "teeth" : teeth, "clearance" : clearance, "internal" : internal, "helical" : helical, "profile_shift" : profile_shift, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, **kwargs})

class _base_radius(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, pressure_angle=None, helical=None, diam_pitch=None, mod=None, pitch=None, **kwargs):
       super().__init__("_base_radius", {"circ_pitch" : circ_pitch, "teeth" : teeth, "pressure_angle" : pressure_angle, "helical" : helical, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, **kwargs})

class bevel_pitch_angle(_Bosl2Base):
    def __init__(self, teeth=None, mate_teeth=None, drive_angle=None, **kwargs):
       super().__init__("bevel_pitch_angle", {"teeth" : teeth, "mate_teeth" : mate_teeth, "drive_angle" : drive_angle, **kwargs})

class worm_gear_thickness(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, worm_diam=None, worm_arc=None, pressure_angle=None, crowning=None, clearance=None, diam_pitch=None, mod=None, pitch=None, **kwargs):
       super().__init__("worm_gear_thickness", {"circ_pitch" : circ_pitch, "teeth" : teeth, "worm_diam" : worm_diam, "worm_arc" : worm_arc, "pressure_angle" : pressure_angle, "crowning" : crowning, "clearance" : clearance, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, **kwargs})

class worm_dist(_Bosl2Base):
    def __init__(self, d=None, starts=None, teeth=None, mod=None, profile_shift=None, diam_pitch=None, circ_pitch=None, pressure_angle=None, backlash=None, **kwargs):
       super().__init__("worm_dist", {"d" : d, "starts" : starts, "teeth" : teeth, "mod" : mod, "profile_shift" : profile_shift, "diam_pitch" : diam_pitch, "circ_pitch" : circ_pitch, "pressure_angle" : pressure_angle, "backlash" : backlash, **kwargs})

class gear_dist(_Bosl2Base):
    def __init__(self, teeth1=None, teeth2=None, helical=None, profile_shift1=None, profile_shift2=None, internal1=None, internal2=None, backlash=None, pressure_angle=None, diam_pitch=None, circ_pitch=None, mod=None, **kwargs):
       super().__init__("gear_dist", {"teeth1" : teeth1, "teeth2" : teeth2, "helical" : helical, "profile_shift1" : profile_shift1, "profile_shift2" : profile_shift2, "internal1" : internal1, "internal2" : internal2, "backlash" : backlash, "pressure_angle" : pressure_angle, "diam_pitch" : diam_pitch, "circ_pitch" : circ_pitch, "mod" : mod, **kwargs})

class _invol(_Bosl2Base):
    def __init__(self, a=None, **kwargs):
       super().__init__("_invol", {"a" : a, **kwargs})

class _working_pressure_angle(_Bosl2Base):
    def __init__(self, teeth1=None, profile_shift1=None, teeth2=None, profile_shift2=None, pressure_angle=None, helical=None, **kwargs):
       super().__init__("_working_pressure_angle", {"teeth1" : teeth1, "profile_shift1" : profile_shift1, "teeth2" : teeth2, "profile_shift2" : profile_shift2, "pressure_angle" : pressure_angle, "helical" : helical, **kwargs})

class gear_dist_skew(_Bosl2Base):
    def __init__(self, teeth1=None, teeth2=None, helical1=None, helical2=None, profile_shift1=None, profile_shift2=None, pressure_angle=None, mod=None, circ_pitch=None, diam_pitch=None, backlash=None, **kwargs):
       super().__init__("gear_dist_skew", {"teeth1" : teeth1, "teeth2" : teeth2, "helical1" : helical1, "helical2" : helical2, "profile_shift1" : profile_shift1, "profile_shift2" : profile_shift2, "pressure_angle" : pressure_angle, "mod" : mod, "circ_pitch" : circ_pitch, "diam_pitch" : diam_pitch, "backlash" : backlash, **kwargs})

class _working_normal_pressure_angle_skew(_Bosl2Base):
    def __init__(self, teeth1=None, profile_shift1=None, helical1=None, teeth2=None, profile_shift2=None, helical2=None, pressure_angle=None, **kwargs):
       super().__init__("_working_normal_pressure_angle_skew", {"teeth1" : teeth1, "profile_shift1" : profile_shift1, "helical1" : helical1, "teeth2" : teeth2, "profile_shift2" : profile_shift2, "helical2" : helical2, "pressure_angle" : pressure_angle, **kwargs})

class gear_skew_angle(_Bosl2Base):
    def __init__(self, teeth1=None, teeth2=None, helical1=None, helical2=None, profile_shift1=None, profile_shift2=None, pressure_angle=None, **kwargs):
       super().__init__("gear_skew_angle", {"teeth1" : teeth1, "teeth2" : teeth2, "helical1" : helical1, "helical2" : helical2, "profile_shift1" : profile_shift1, "profile_shift2" : profile_shift2, "pressure_angle" : pressure_angle, **kwargs})

class get_profile_shift(_Bosl2Base):
    def __init__(self, desired=None, teeth1=None, teeth2=None, helical=None, pressure_angle=None, mod=None, diam_pitch=None, circ_pitch=None, **kwargs):
       super().__init__("get_profile_shift", {"desired" : desired, "teeth1" : teeth1, "teeth2" : teeth2, "helical" : helical, "pressure_angle" : pressure_angle, "mod" : mod, "diam_pitch" : diam_pitch, "circ_pitch" : circ_pitch, **kwargs})

class auto_profile_shift(_Bosl2Base):
    def __init__(self, teeth=None, pressure_angle=None, helical=None, min_teeth=None, profile_shift=None, get_min=None, **kwargs):
       super().__init__("auto_profile_shift", {"teeth" : teeth, "pressure_angle" : pressure_angle, "helical" : helical, "min_teeth" : min_teeth, "profile_shift" : profile_shift, "get_min" : get_min, **kwargs})

class gear_shorten(_Bosl2Base):
    def __init__(self, teeth1=None, teeth2=None, helical=None, profile_shift1=None, profile_shift2=None, pressure_angle=None, **kwargs):
       super().__init__("gear_shorten", {"teeth1" : teeth1, "teeth2" : teeth2, "helical" : helical, "profile_shift1" : profile_shift1, "profile_shift2" : profile_shift2, "pressure_angle" : pressure_angle, **kwargs})

class gear_shorten_skew(_Bosl2Base):
    def __init__(self, teeth1=None, teeth2=None, helical1=None, helical2=None, profile_shift1=None, profile_shift2=None, pressure_angle=None, **kwargs):
       super().__init__("gear_shorten_skew", {"teeth1" : teeth1, "teeth2" : teeth2, "helical1" : helical1, "helical2" : helical2, "profile_shift1" : profile_shift1, "profile_shift2" : profile_shift2, "pressure_angle" : pressure_angle, **kwargs})

class spur_gear(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, thickness=None, shaft_diam=None, hide=None, pressure_angle=None, clearance=None, backlash=None, helical=None, internal=None, interior=None, profile_shift=None, slices=None, herringbone=None, shorten=None, pitch=None, diam_pitch=None, mod=None, atype=None, gear_spin=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spur_gear", {"circ_pitch" : circ_pitch, "teeth" : teeth, "thickness" : thickness, "shaft_diam" : shaft_diam, "hide" : hide, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "helical" : helical, "internal" : internal, "interior" : interior, "profile_shift" : profile_shift, "slices" : slices, "herringbone" : herringbone, "shorten" : shorten, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "atype" : atype, "gear_spin" : gear_spin, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class spur_gear2d(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, hide=None, pressure_angle=None, clearance=None, backlash=None, internal=None, interior=None, profile_shift=None, helical=None, shorten=None, shaft_diam=None, pitch=None, diam_pitch=None, mod=None, gear_spin=None, atype=None, anchor=None, spin=None, **kwargs):
       super().__init__("spur_gear2d", {"circ_pitch" : circ_pitch, "teeth" : teeth, "hide" : hide, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "internal" : internal, "interior" : interior, "profile_shift" : profile_shift, "helical" : helical, "shorten" : shorten, "shaft_diam" : shaft_diam, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "gear_spin" : gear_spin, "atype" : atype, "anchor" : anchor, "spin" : spin, **kwargs})

class ring_gear(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, thickness=None, backing=None, pressure_angle=None, helical=None, herringbone=None, profile_shift=None, clearance=None, backlash=None, _or=None, od=None, width=None, pitch=None, diam_pitch=None, mod=None, slices=None, gear_spin=None, anchor=None, atype=None, spin=None, orient=None, **kwargs):
       super().__init__("ring_gear", {"circ_pitch" : circ_pitch, "teeth" : teeth, "thickness" : thickness, "backing" : backing, "pressure_angle" : pressure_angle, "helical" : helical, "herringbone" : herringbone, "profile_shift" : profile_shift, "clearance" : clearance, "backlash" : backlash, "_or" : _or, "od" : od, "width" : width, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "slices" : slices, "gear_spin" : gear_spin, "anchor" : anchor, "atype" : atype, "spin" : spin, "orient" : orient, **kwargs})

class ring_gear2d(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, backing=None, pressure_angle=None, helical=None, profile_shift=None, clearance=None, backlash=None, _or=None, od=None, width=None, pitch=None, diam_pitch=None, mod=None, atype=None, gear_spin=None, shorten=None, anchor=None, spin=None, **kwargs):
       super().__init__("ring_gear2d", {"circ_pitch" : circ_pitch, "teeth" : teeth, "backing" : backing, "pressure_angle" : pressure_angle, "helical" : helical, "profile_shift" : profile_shift, "clearance" : clearance, "backlash" : backlash, "_or" : _or, "od" : od, "width" : width, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "atype" : atype, "gear_spin" : gear_spin, "shorten" : shorten, "anchor" : anchor, "spin" : spin, **kwargs})

class rack(_Bosl2Base):
    def __init__(self, pitch=None, teeth=None, thickness=None, backing=None, width=None, bottom=None, pressure_angle=None, backlash=None, clearance=None, helical=None, herringbone=None, profile_shift=None, gear_travel=None, circ_pitch=None, diam_pitch=None, mod=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rack", {"pitch" : pitch, "teeth" : teeth, "thickness" : thickness, "backing" : backing, "width" : width, "bottom" : bottom, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "helical" : helical, "herringbone" : herringbone, "profile_shift" : profile_shift, "gear_travel" : gear_travel, "circ_pitch" : circ_pitch, "diam_pitch" : diam_pitch, "mod" : mod, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rack2d(_Bosl2Base):
    def __init__(self, pitch=None, teeth=None, backing=None, width=None, bottom=None, pressure_angle=None, backlash=None, clearance=None, helical=None, profile_shift=None, gear_travel=None, circ_pitch=None, diam_pitch=None, mod=None, rounding=None, anchor=None, spin=None, **kwargs):
       super().__init__("rack2d", {"pitch" : pitch, "teeth" : teeth, "backing" : backing, "width" : width, "bottom" : bottom, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "helical" : helical, "profile_shift" : profile_shift, "gear_travel" : gear_travel, "circ_pitch" : circ_pitch, "diam_pitch" : diam_pitch, "mod" : mod, "rounding" : rounding, "anchor" : anchor, "spin" : spin, **kwargs})

class crown_gear(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, backing=None, face_width=None, pressure_angle=None, clearance=None, backlash=None, profile_shift=None, slices=None, bottom=None, thickness=None, diam_pitch=None, pitch=None, mod=None, gear_spin=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("crown_gear", {"circ_pitch" : circ_pitch, "teeth" : teeth, "backing" : backing, "face_width" : face_width, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "profile_shift" : profile_shift, "slices" : slices, "bottom" : bottom, "thickness" : thickness, "diam_pitch" : diam_pitch, "pitch" : pitch, "mod" : mod, "gear_spin" : gear_spin, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class bevel_gear(_Bosl2Base):
    def __init__(self, teeth=None, mate_teeth=None, shaft_angle=None, bottom=None, backing=None, thickness=None, cone_backing=None, face_width=None, shaft_diam=None, pressure_angle=None, clearance=None, backlash=None, cutter_radius=None, spiral=None, right_handed=None, slices=None, pitch=None, diam_pitch=None, circ_pitch=None, mod=None, anchor=None, spin=None, gear_spin=None, orient=None, **kwargs):
       super().__init__("bevel_gear", {"teeth" : teeth, "mate_teeth" : mate_teeth, "shaft_angle" : shaft_angle, "bottom" : bottom, "backing" : backing, "thickness" : thickness, "cone_backing" : cone_backing, "face_width" : face_width, "shaft_diam" : shaft_diam, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "cutter_radius" : cutter_radius, "spiral" : spiral, "right_handed" : right_handed, "slices" : slices, "pitch" : pitch, "diam_pitch" : diam_pitch, "circ_pitch" : circ_pitch, "mod" : mod, "anchor" : anchor, "spin" : spin, "gear_spin" : gear_spin, "orient" : orient, **kwargs})

class worm(_Bosl2Base):
    def __init__(self, circ_pitch=None, d=None, l=None, starts=None, left_handed=None, pressure_angle=None, backlash=None, clearance=None, pitch=None, diam_pitch=None, mod=None, gear_spin=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("worm", {"circ_pitch" : circ_pitch, "d" : d, "l" : l, "starts" : starts, "left_handed" : left_handed, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "gear_spin" : gear_spin, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class enveloping_worm(_Bosl2Base):
    def __init__(self, circ_pitch=None, mate_teeth=None, d=None, left_handed=None, starts=None, arc=None, pressure_angle=None, gear_spin=None, rounding=None, taper=None, diam_pitch=None, mod=None, pitch=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("enveloping_worm", {"circ_pitch" : circ_pitch, "mate_teeth" : mate_teeth, "d" : d, "left_handed" : left_handed, "starts" : starts, "arc" : arc, "pressure_angle" : pressure_angle, "gear_spin" : gear_spin, "rounding" : rounding, "taper" : taper, "diam_pitch" : diam_pitch, "mod" : mod, "pitch" : pitch, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class worm_gear(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, worm_diam=None, worm_starts=None, worm_arc=None, crowning=None, left_handed=None, pressure_angle=None, backlash=None, clearance=None, profile_shift=None, slices=None, shaft_diam=None, gear_spin=None, pitch=None, diam_pitch=None, mod=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("worm_gear", {"circ_pitch" : circ_pitch, "teeth" : teeth, "worm_diam" : worm_diam, "worm_starts" : worm_starts, "worm_arc" : worm_arc, "crowning" : crowning, "left_handed" : left_handed, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "profile_shift" : profile_shift, "slices" : slices, "shaft_diam" : shaft_diam, "gear_spin" : gear_spin, "pitch" : pitch, "diam_pitch" : diam_pitch, "mod" : mod, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _show_gear_tooth_profile(_Bosl2Base):
    def __init__(self, circ_pitch=None, teeth=None, pressure_angle=None, profile_shift=None, helical=None, internal=None, clearance=None, backlash=None, show_verts=None, diam_pitch=None, mod=None, **kwargs):
       super().__init__("_show_gear_tooth_profile", {"circ_pitch" : circ_pitch, "teeth" : teeth, "pressure_angle" : pressure_angle, "profile_shift" : profile_shift, "helical" : helical, "internal" : internal, "clearance" : clearance, "backlash" : backlash, "show_verts" : show_verts, "diam_pitch" : diam_pitch, "mod" : mod, **kwargs})

