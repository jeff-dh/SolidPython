from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/shapes2d.scad'}", False)

class square(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, **kwargs):
       super().__init__("square", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, **kwargs})

class rect(_Bosl2Base):
    def __init__(self, size=None, rounding=None, chamfer=None, atype=None, anchor=None, spin=None, _return_override=None, corner_flip=None, **kwargs):
       super().__init__("rect", {"size" : size, "rounding" : rounding, "chamfer" : chamfer, "atype" : atype, "anchor" : anchor, "spin" : spin, "_return_override" : _return_override, "corner_flip" : corner_flip, **kwargs})

class circle(_Bosl2Base):
    def __init__(self, r=None, d=None, points=None, corner=None, anchor=None, spin=None, **kwargs):
       super().__init__("circle", {"r" : r, "d" : d, "points" : points, "corner" : corner, "anchor" : anchor, "spin" : spin, **kwargs})

class _ellipse_refine(_Bosl2Base):
    def __init__(self, a=None, b=None, N=None, _theta=None, **kwargs):
       super().__init__("_ellipse_refine", {"a" : a, "b" : b, "N" : N, "_theta" : _theta, **kwargs})

class _ellipse_refine_realign(_Bosl2Base):
    def __init__(self, a=None, b=None, N=None, _theta=None, i=None, **kwargs):
       super().__init__("_ellipse_refine_realign", {"a" : a, "b" : b, "N" : N, "_theta" : _theta, "i" : i, **kwargs})

class ellipse(_Bosl2Base):
    def __init__(self, r=None, d=None, realign=None, circum=None, uniform=None, anchor=None, spin=None, **kwargs):
       super().__init__("ellipse", {"r" : r, "d" : d, "realign" : realign, "circum" : circum, "uniform" : uniform, "anchor" : anchor, "spin" : spin, **kwargs})

class regular_ngon(_Bosl2Base):
    def __init__(self, n=None, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, _mat=None, _anchs=None, **kwargs):
       super().__init__("regular_ngon", {"n" : n, "r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, "_mat" : _mat, "_anchs" : _anchs, **kwargs})

class pentagon(_Bosl2Base):
    def __init__(self, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, **kwargs):
       super().__init__("pentagon", {"r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, **kwargs})

class hexagon(_Bosl2Base):
    def __init__(self, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, **kwargs):
       super().__init__("hexagon", {"r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, **kwargs})

class octagon(_Bosl2Base):
    def __init__(self, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, **kwargs):
       super().__init__("octagon", {"r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, **kwargs})

class right_triangle(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, **kwargs):
       super().__init__("right_triangle", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, **kwargs})

class _trapezoid_dims(_Bosl2Base):
    def __init__(self, h=None, w1=None, w2=None, shift=None, ang=None, **kwargs):
       super().__init__("_trapezoid_dims", {"h" : h, "w1" : w1, "w2" : w2, "shift" : shift, "ang" : ang, **kwargs})

class trapezoid(_Bosl2Base):
    def __init__(self, h=None, w1=None, w2=None, ang=None, shift=None, chamfer=None, rounding=None, flip=None, anchor=None, spin=None, atype=None, _return_override=None, angle=None, **kwargs):
       super().__init__("trapezoid", {"h" : h, "w1" : w1, "w2" : w2, "ang" : ang, "shift" : shift, "chamfer" : chamfer, "rounding" : rounding, "flip" : flip, "anchor" : anchor, "spin" : spin, "atype" : atype, "_return_override" : _return_override, "angle" : angle, **kwargs})

class star(_Bosl2Base):
    def __init__(self, n=None, r=None, ir=None, d=None, _or=None, od=None, id=None, step=None, realign=None, align_tip=None, align_pit=None, anchor=None, spin=None, atype=None, _mat=None, _anchs=None, **kwargs):
       super().__init__("star", {"n" : n, "r" : r, "ir" : ir, "d" : d, "_or" : _or, "od" : od, "id" : id, "step" : step, "realign" : realign, "align_tip" : align_tip, "align_pit" : align_pit, "anchor" : anchor, "spin" : spin, "atype" : atype, "_mat" : _mat, "_anchs" : _anchs, **kwargs})

class _path_add_jitter(_Bosl2Base):
    def __init__(self, path=None, dist=None, closed=None, **kwargs):
       super().__init__("_path_add_jitter", {"path" : path, "dist" : dist, "closed" : closed, **kwargs})

class teardrop2d(_Bosl2Base):
    def __init__(self, r=None, ang=None, cap_h=None, d=None, circum=None, realign=None, anchor=None, spin=None, bot_corner=None, _extrapt=None, **kwargs):
       super().__init__("teardrop2d", {"r" : r, "ang" : ang, "cap_h" : cap_h, "d" : d, "circum" : circum, "realign" : realign, "anchor" : anchor, "spin" : spin, "bot_corner" : bot_corner, "_extrapt" : _extrapt, **kwargs})

class egg(_Bosl2Base):
    def __init__(self, length=None, r1=None, r2=None, R=None, d1=None, d2=None, D=None, anchor=None, spin=None, **kwargs):
       super().__init__("egg", {"length" : length, "r1" : r1, "r2" : r2, "R" : R, "d1" : d1, "d2" : d2, "D" : D, "anchor" : anchor, "spin" : spin, **kwargs})

class ring(_Bosl2Base):
    def __init__(self, n=None, ring_width=None, r=None, r1=None, r2=None, angle=None, d=None, d1=None, d2=None, cp=None, points=None, corner=None, width=None, thickness=None, start=None, long=None, full=None, cw=None, ccw=None, **kwargs):
       super().__init__("ring", {"n" : n, "ring_width" : ring_width, "r" : r, "r1" : r1, "r2" : r2, "angle" : angle, "d" : d, "d1" : d1, "d2" : d2, "cp" : cp, "points" : points, "corner" : corner, "width" : width, "thickness" : thickness, "start" : start, "long" : long, "full" : full, "cw" : cw, "ccw" : ccw, **kwargs})

class glued_circles(_Bosl2Base):
    def __init__(self, r=None, spread=None, tangent=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("glued_circles", {"r" : r, "spread" : spread, "tangent" : tangent, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class squircle(_Bosl2Base):
    def __init__(self, size=None, squareness=None, style=None, anchor=None, spin=None, atype=None, **kwargs):
       super().__init__("squircle", {"size" : size, "squareness" : squareness, "style" : style, "anchor" : anchor, "spin" : spin, "atype" : atype, **kwargs})

class _squircle_fg(_Bosl2Base):
    def __init__(self, size=None, squareness=None, **kwargs):
       super().__init__("_squircle_fg", {"size" : size, "squareness" : squareness, **kwargs})

class squircle_radius_fg(_Bosl2Base):
    def __init__(self, squareness=None, r=None, angle=None, **kwargs):
       super().__init__("squircle_radius_fg", {"squareness" : squareness, "r" : r, "angle" : angle, **kwargs})

class _linearize_squareness(_Bosl2Base):
    def __init__(self, s=None, **kwargs):
       super().__init__("_linearize_squareness", {"s" : s, **kwargs})

class _squircle_se(_Bosl2Base):
    def __init__(self, size=None, squareness=None, **kwargs):
       super().__init__("_squircle_se", {"size" : size, "squareness" : squareness, **kwargs})

class squircle_radius_se(_Bosl2Base):
    def __init__(self, n=None, r=None, angle=None, **kwargs):
       super().__init__("squircle_radius_se", {"n" : n, "r" : r, "angle" : angle, **kwargs})

class _squircle_se_exponent(_Bosl2Base):
    def __init__(self, squareness=None, **kwargs):
       super().__init__("_squircle_se_exponent", {"squareness" : squareness, **kwargs})

class _squircle_bz(_Bosl2Base):
    def __init__(self, size=None, squareness=None, **kwargs):
       super().__init__("_squircle_bz", {"size" : size, "squareness" : squareness, **kwargs})

class keyhole(_Bosl2Base):
    def __init__(self, l=None, r1=None, r2=None, shoulder_r=None, d1=None, d2=None, length=None, anchor=None, spin=None, **kwargs):
       super().__init__("keyhole", {"l" : l, "r1" : r1, "r2" : r2, "shoulder_r" : shoulder_r, "d1" : d1, "d2" : d2, "length" : length, "anchor" : anchor, "spin" : spin, **kwargs})

class reuleaux_polygon(_Bosl2Base):
    def __init__(self, n=None, r=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("reuleaux_polygon", {"n" : n, "r" : r, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class supershape(_Bosl2Base):
    def __init__(self, step=None, n=None, m1=None, m2=None, n1=None, n2=None, n3=None, a=None, b=None, r=None, d=None, anchor=None, spin=None, atype=None, **kwargs):
       super().__init__("supershape", {"step" : step, "n" : n, "m1" : m1, "m2" : m2, "n1" : n1, "n2" : n2, "n3" : n3, "a" : a, "b" : b, "r" : r, "d" : d, "anchor" : anchor, "spin" : spin, "atype" : atype, **kwargs})

class _superformula(_Bosl2Base):
    def __init__(self, theta=None, m1=None, m2=None, n1=None, n2=None, n3=None, a=None, b=None, **kwargs):
       super().__init__("_superformula", {"theta" : theta, "m1" : m1, "m2" : m2, "n1" : n1, "n2" : n2, "n3" : n3, "a" : a, "b" : b, **kwargs})

class square(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, **kwargs):
       super().__init__("square", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, **kwargs})

class rect(_Bosl2Base):
    def __init__(self, size=None, rounding=None, atype=None, chamfer=None, anchor=None, spin=None, corner_flip=None, **kwargs):
       super().__init__("rect", {"size" : size, "rounding" : rounding, "atype" : atype, "chamfer" : chamfer, "anchor" : anchor, "spin" : spin, "corner_flip" : corner_flip, **kwargs})

class circle(_Bosl2Base):
    def __init__(self, r=None, d=None, points=None, corner=None, anchor=None, spin=None, **kwargs):
       super().__init__("circle", {"r" : r, "d" : d, "points" : points, "corner" : corner, "anchor" : anchor, "spin" : spin, **kwargs})

class ellipse(_Bosl2Base):
    def __init__(self, r=None, d=None, realign=None, circum=None, uniform=None, anchor=None, spin=None, **kwargs):
       super().__init__("ellipse", {"r" : r, "d" : d, "realign" : realign, "circum" : circum, "uniform" : uniform, "anchor" : anchor, "spin" : spin, **kwargs})

class regular_ngon(_Bosl2Base):
    def __init__(self, n=None, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, **kwargs):
       super().__init__("regular_ngon", {"n" : n, "r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, **kwargs})

class pentagon(_Bosl2Base):
    def __init__(self, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, **kwargs):
       super().__init__("pentagon", {"r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, **kwargs})

class hexagon(_Bosl2Base):
    def __init__(self, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, **kwargs):
       super().__init__("hexagon", {"r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, **kwargs})

class octagon(_Bosl2Base):
    def __init__(self, r=None, d=None, _or=None, od=None, ir=None, id=None, side=None, rounding=None, realign=None, align_tip=None, align_side=None, anchor=None, spin=None, **kwargs):
       super().__init__("octagon", {"r" : r, "d" : d, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "side" : side, "rounding" : rounding, "realign" : realign, "align_tip" : align_tip, "align_side" : align_side, "anchor" : anchor, "spin" : spin, **kwargs})

class right_triangle(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, **kwargs):
       super().__init__("right_triangle", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, **kwargs})

class trapezoid(_Bosl2Base):
    def __init__(self, h=None, w1=None, w2=None, ang=None, shift=None, chamfer=None, rounding=None, flip=None, anchor=None, spin=None, atype=None, angle=None, **kwargs):
       super().__init__("trapezoid", {"h" : h, "w1" : w1, "w2" : w2, "ang" : ang, "shift" : shift, "chamfer" : chamfer, "rounding" : rounding, "flip" : flip, "anchor" : anchor, "spin" : spin, "atype" : atype, "angle" : angle, **kwargs})

class star(_Bosl2Base):
    def __init__(self, n=None, r=None, ir=None, d=None, _or=None, od=None, id=None, step=None, realign=None, align_tip=None, align_pit=None, anchor=None, spin=None, atype=None, **kwargs):
       super().__init__("star", {"n" : n, "r" : r, "ir" : ir, "d" : d, "_or" : _or, "od" : od, "id" : id, "step" : step, "realign" : realign, "align_tip" : align_tip, "align_pit" : align_pit, "anchor" : anchor, "spin" : spin, "atype" : atype, **kwargs})

class jittered_poly(_Bosl2Base):
    def __init__(self, path=None, dist=None, **kwargs):
       super().__init__("jittered_poly", {"path" : path, "dist" : dist, **kwargs})

class teardrop2d(_Bosl2Base):
    def __init__(self, r=None, ang=None, cap_h=None, d=None, circum=None, realign=None, bot_corner=None, anchor=None, spin=None, **kwargs):
       super().__init__("teardrop2d", {"r" : r, "ang" : ang, "cap_h" : cap_h, "d" : d, "circum" : circum, "realign" : realign, "bot_corner" : bot_corner, "anchor" : anchor, "spin" : spin, **kwargs})

class egg(_Bosl2Base):
    def __init__(self, length=None, r1=None, r2=None, R=None, d1=None, d2=None, D=None, anchor=None, spin=None, **kwargs):
       super().__init__("egg", {"length" : length, "r1" : r1, "r2" : r2, "R" : R, "d1" : d1, "d2" : d2, "D" : D, "anchor" : anchor, "spin" : spin, **kwargs})

class ring(_Bosl2Base):
    def __init__(self, n=None, ring_width=None, r=None, r1=None, r2=None, angle=None, d=None, d1=None, d2=None, cp=None, points=None, corner=None, width=None, thickness=None, start=None, long=None, full=None, cw=None, ccw=None, anchor=None, spin=None, **kwargs):
       super().__init__("ring", {"n" : n, "ring_width" : ring_width, "r" : r, "r1" : r1, "r2" : r2, "angle" : angle, "d" : d, "d1" : d1, "d2" : d2, "cp" : cp, "points" : points, "corner" : corner, "width" : width, "thickness" : thickness, "start" : start, "long" : long, "full" : full, "cw" : cw, "ccw" : ccw, "anchor" : anchor, "spin" : spin, **kwargs})

class glued_circles(_Bosl2Base):
    def __init__(self, r=None, spread=None, tangent=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("glued_circles", {"r" : r, "spread" : spread, "tangent" : tangent, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class squircle(_Bosl2Base):
    def __init__(self, size=None, squareness=None, style=None, anchor=None, spin=None, atype=None, **kwargs):
       super().__init__("squircle", {"size" : size, "squareness" : squareness, "style" : style, "anchor" : anchor, "spin" : spin, "atype" : atype, **kwargs})

class keyhole(_Bosl2Base):
    def __init__(self, l=None, r1=None, r2=None, shoulder_r=None, d1=None, d2=None, length=None, anchor=None, spin=None, **kwargs):
       super().__init__("keyhole", {"l" : l, "r1" : r1, "r2" : r2, "shoulder_r" : shoulder_r, "d1" : d1, "d2" : d2, "length" : length, "anchor" : anchor, "spin" : spin, **kwargs})

class reuleaux_polygon(_Bosl2Base):
    def __init__(self, n=None, r=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("reuleaux_polygon", {"n" : n, "r" : r, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class supershape(_Bosl2Base):
    def __init__(self, step=None, n=None, m1=None, m2=None, n1=None, n2=None, n3=None, a=None, b=None, r=None, d=None, anchor=None, spin=None, atype=None, **kwargs):
       super().__init__("supershape", {"step" : step, "n" : n, "m1" : m1, "m2" : m2, "n1" : n1, "n2" : n2, "n3" : n3, "a" : a, "b" : b, "r" : r, "d" : d, "anchor" : anchor, "spin" : spin, "atype" : atype, **kwargs})

class text(_Bosl2Base):
    def __init__(self, text=None, size=None, font=None, halign=None, valign=None, spacing=None, direction=None, language=None, script=None, anchor=None, spin=None, **kwargs):
       super().__init__("text", {"text" : text, "size" : size, "font" : font, "halign" : halign, "valign" : valign, "spacing" : spacing, "direction" : direction, "language" : language, "script" : script, "anchor" : anchor, "spin" : spin, **kwargs})

class round2d(_Bosl2Base):
    def __init__(self, r=None, _or=None, ir=None, **kwargs):
       super().__init__("round2d", {"r" : r, "_or" : _or, "ir" : ir, **kwargs})

class shell2d(_Bosl2Base):
    def __init__(self, thickness=None, _or=None, ir=None, **kwargs):
       super().__init__("shell2d", {"thickness" : thickness, "_or" : _or, "ir" : ir, **kwargs})

