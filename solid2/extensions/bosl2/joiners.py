from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/joiners.scad'}", False)

class half_joiner_clear(_Bosl2Base):
    def __init__(self, l=None, w=None, ang=None, clearance=None, overlap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("half_joiner_clear", {"l" : l, "w" : w, "ang" : ang, "clearance" : clearance, "overlap" : overlap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class half_joiner(_Bosl2Base):
    def __init__(self, l=None, w=None, base=None, ang=None, screwsize=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("half_joiner", {"l" : l, "w" : w, "base" : base, "ang" : ang, "screwsize" : screwsize, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class half_joiner2(_Bosl2Base):
    def __init__(self, l=None, w=None, base=None, ang=None, screwsize=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("half_joiner2", {"l" : l, "w" : w, "base" : base, "ang" : ang, "screwsize" : screwsize, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class joiner_clear(_Bosl2Base):
    def __init__(self, l=None, w=None, ang=None, clearance=None, overlap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("joiner_clear", {"l" : l, "w" : w, "ang" : ang, "clearance" : clearance, "overlap" : overlap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class joiner(_Bosl2Base):
    def __init__(self, l=None, w=None, base=None, ang=None, screwsize=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("joiner", {"l" : l, "w" : w, "base" : base, "ang" : ang, "screwsize" : screwsize, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class dovetail(_Bosl2Base):
    def __init__(self, gender=None, width=None, height=None, slide=None, h=None, w=None, angle=None, slope=None, thickness=None, taper=None, back_width=None, chamfer=None, extra=None, r=None, radius=None, round=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("dovetail", {"gender" : gender, "width" : width, "height" : height, "slide" : slide, "h" : h, "w" : w, "angle" : angle, "slope" : slope, "thickness" : thickness, "taper" : taper, "back_width" : back_width, "chamfer" : chamfer, "extra" : extra, "r" : r, "radius" : radius, "round" : round, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _pin_size(_Bosl2Base):
    def __init__(self, size=None, **kwargs):
       super().__init__("_pin_size", {"size" : size, **kwargs})

class snap_pin(_Bosl2Base):
    def __init__(self, size=None, r=None, radius=None, d=None, diameter=None, l=None, length=None, nub_depth=None, snap=None, thickness=None, clearance=None, preload=None, pointed=None, anchor=None, spin=None, orient=None, center=None, **kwargs):
       super().__init__("snap_pin", {"size" : size, "r" : r, "radius" : radius, "d" : d, "diameter" : diameter, "l" : l, "length" : length, "nub_depth" : nub_depth, "snap" : snap, "thickness" : thickness, "clearance" : clearance, "preload" : preload, "pointed" : pointed, "anchor" : anchor, "spin" : spin, "orient" : orient, "center" : center, **kwargs})

class snap_pin_socket(_Bosl2Base):
    def __init__(self, size=None, r=None, radius=None, l=None, length=None, d=None, diameter=None, nub_depth=None, snap=None, fixed=None, pointed=None, fins=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("snap_pin_socket", {"size" : size, "r" : r, "radius" : radius, "l" : l, "length" : length, "d" : d, "diameter" : diameter, "nub_depth" : nub_depth, "snap" : snap, "fixed" : fixed, "pointed" : pointed, "fins" : fins, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rabbit_clip(_Bosl2Base):
    def __init__(self, type=None, length=None, width=None, snap=None, thickness=None, depth=None, compression=None, clearance=None, lock=None, lock_clearance=None, splinesteps=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("rabbit_clip", {"type" : type, "length" : length, "width" : width, "snap" : snap, "thickness" : thickness, "depth" : depth, "compression" : compression, "clearance" : clearance, "lock" : lock, "lock_clearance" : lock_clearance, "splinesteps" : splinesteps, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})

class half_joiner_clear(_Bosl2Base):
    def __init__(self, l=None, w=None, ang=None, clearance=None, overlap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("half_joiner_clear", {"l" : l, "w" : w, "ang" : ang, "clearance" : clearance, "overlap" : overlap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class half_joiner(_Bosl2Base):
    def __init__(self, l=None, w=None, base=None, ang=None, screwsize=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("half_joiner", {"l" : l, "w" : w, "base" : base, "ang" : ang, "screwsize" : screwsize, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class half_joiner2(_Bosl2Base):
    def __init__(self, l=None, w=None, base=None, ang=None, screwsize=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("half_joiner2", {"l" : l, "w" : w, "base" : base, "ang" : ang, "screwsize" : screwsize, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class joiner_clear(_Bosl2Base):
    def __init__(self, l=None, w=None, ang=None, clearance=None, overlap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("joiner_clear", {"l" : l, "w" : w, "ang" : ang, "clearance" : clearance, "overlap" : overlap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class joiner(_Bosl2Base):
    def __init__(self, l=None, w=None, base=None, ang=None, screwsize=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("joiner", {"l" : l, "w" : w, "base" : base, "ang" : ang, "screwsize" : screwsize, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class dovetail(_Bosl2Base):
    def __init__(self, gender=None, width=None, height=None, slide=None, h=None, w=None, angle=None, slope=None, thickness=None, taper=None, back_width=None, chamfer=None, extra=None, r=None, radius=None, round=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("dovetail", {"gender" : gender, "width" : width, "height" : height, "slide" : slide, "h" : h, "w" : w, "angle" : angle, "slope" : slope, "thickness" : thickness, "taper" : taper, "back_width" : back_width, "chamfer" : chamfer, "extra" : extra, "r" : r, "radius" : radius, "round" : round, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _pin_nub(_Bosl2Base):
    def __init__(self, r=None, nub=None, h=None, **kwargs):
       super().__init__("_pin_nub", {"r" : r, "nub" : nub, "h" : h, **kwargs})

class _pin_slot(_Bosl2Base):
    def __init__(self, l=None, r=None, t=None, d=None, nub=None, depth=None, stretch=None, **kwargs):
       super().__init__("_pin_slot", {"l" : l, "r" : r, "t" : t, "d" : d, "nub" : nub, "depth" : depth, "stretch" : stretch, **kwargs})

class _pin_shaft(_Bosl2Base):
    def __init__(self, r=None, lStraight=None, nub=None, nubscale=None, stretch=None, d=None, pointed=None, **kwargs):
       super().__init__("_pin_shaft", {"r" : r, "lStraight" : lStraight, "nub" : nub, "nubscale" : nubscale, "stretch" : stretch, "d" : d, "pointed" : pointed, **kwargs})

class snap_pin(_Bosl2Base):
    def __init__(self, size=None, r=None, radius=None, d=None, diameter=None, l=None, length=None, nub_depth=None, snap=None, thickness=None, clearance=None, preload=None, pointed=None, anchor=None, spin=None, orient=None, center=None, **kwargs):
       super().__init__("snap_pin", {"size" : size, "r" : r, "radius" : radius, "d" : d, "diameter" : diameter, "l" : l, "length" : length, "nub_depth" : nub_depth, "snap" : snap, "thickness" : thickness, "clearance" : clearance, "preload" : preload, "pointed" : pointed, "anchor" : anchor, "spin" : spin, "orient" : orient, "center" : center, **kwargs})

class snap_pin_socket(_Bosl2Base):
    def __init__(self, size=None, r=None, radius=None, l=None, length=None, d=None, diameter=None, nub_depth=None, snap=None, fixed=None, pointed=None, fins=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("snap_pin_socket", {"size" : size, "r" : r, "radius" : radius, "l" : l, "length" : length, "d" : d, "diameter" : diameter, "nub_depth" : nub_depth, "snap" : snap, "fixed" : fixed, "pointed" : pointed, "fins" : fins, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rabbit_clip(_Bosl2Base):
    def __init__(self, type=None, length=None, width=None, snap=None, thickness=None, depth=None, compression=None, clearance=None, lock=None, lock_clearance=None, splinesteps=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("rabbit_clip", {"type" : type, "length" : length, "width" : width, "snap" : snap, "thickness" : thickness, "depth" : depth, "compression" : compression, "clearance" : clearance, "lock" : lock, "lock_clearance" : lock_clearance, "splinesteps" : splinesteps, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})

class hirth(_Bosl2Base):
    def __init__(self, n=None, ir=None, _or=None, id=None, od=None, tooth_angle=None, cone_angle=None, chamfer=None, rounding=None, base=None, crop=None, skew=None, rot=None, orient=None, anchor=None, spin=None, **kwargs):
       super().__init__("hirth", {"n" : n, "ir" : ir, "_or" : _or, "id" : id, "od" : od, "tooth_angle" : tooth_angle, "cone_angle" : cone_angle, "chamfer" : chamfer, "rounding" : rounding, "base" : base, "crop" : crop, "skew" : skew, "rot" : rot, "orient" : orient, "anchor" : anchor, "spin" : spin, **kwargs})

