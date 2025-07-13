from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/shapes3d.scad'}", False)

class cube(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cube", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cuboid(_Bosl2Base):
    def __init__(self, size=None, p1=None, p2=None, chamfer=None, rounding=None, edges=None, except_edges=None, trimcorners=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cuboid", {"size" : size, "p1" : p1, "p2" : p2, "chamfer" : chamfer, "rounding" : rounding, "edges" : edges, "except_edges" : except_edges, "trimcorners" : trimcorners, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class prismoid(_Bosl2Base):
    def __init__(self, size1=None, size2=None, h=None, shift=None, rounding=None, rounding1=None, rounding2=None, chamfer=None, chamfer1=None, chamfer2=None, l=None, height=None, length=None, center=None, anchor=None, spin=None, orient=None, xang=None, yang=None, _return_dim=None, **kwargs):
       super().__init__("prismoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "l" : l, "height" : height, "length" : length, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, "xang" : xang, "yang" : yang, "_return_dim" : _return_dim, **kwargs})

class regular_prism(_Bosl2Base):
    def __init__(self, n=None, h=None, r=None, center=None, l=None, length=None, height=None, r1=None, r2=None, ir=None, ir1=None, ir2=None, _or=None, or1=None, or2=None, side=None, side1=None, side2=None, d=None, d1=None, d2=None, id=None, id1=None, id2=None, od=None, od1=None, od2=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, shift=None, teardrop=None, clip_angle=None, from_end=None, from_end1=None, from_end2=None, texture=None, tex_size=None, tex_reps=None, tex_inset=None, tex_rot=None, tex_depth=None, tex_samples=None, tex_taper=None, style=None, anchor=None, spin=None, orient=None, _return_anchors=None, **kwargs):
       super().__init__("regular_prism", {"n" : n, "h" : h, "r" : r, "center" : center, "l" : l, "length" : length, "height" : height, "r1" : r1, "r2" : r2, "ir" : ir, "ir1" : ir1, "ir2" : ir2, "_or" : _or, "or1" : or1, "or2" : or2, "side" : side, "side1" : side1, "side2" : side2, "d" : d, "d1" : d1, "d2" : d2, "id" : id, "id1" : id1, "id2" : id2, "od" : od, "od1" : od1, "od2" : od2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "shift" : shift, "teardrop" : teardrop, "clip_angle" : clip_angle, "from_end" : from_end, "from_end1" : from_end1, "from_end2" : from_end2, "texture" : texture, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "tex_samples" : tex_samples, "tex_taper" : tex_taper, "style" : style, "anchor" : anchor, "spin" : spin, "orient" : orient, "_return_anchors" : _return_anchors, **kwargs})

class textured_tile(_Bosl2Base):
    def __init__(self, texture=None, size=None, ysize=None, height=None, w1=None, w2=None, ang=None, h=None, shift=None, thickness=None, tex_size=None, tex_reps=None, tex_inset=None, tex_rot=None, tex_depth=None, style=None, atype=None, tex_extra=None, tex_skip=None, anchor=None, spin=None, orient=None, _return_anchor=None, **kwargs):
       super().__init__("textured_tile", {"texture" : texture, "size" : size, "ysize" : ysize, "height" : height, "w1" : w1, "w2" : w2, "ang" : ang, "h" : h, "shift" : shift, "thickness" : thickness, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "style" : style, "atype" : atype, "tex_extra" : tex_extra, "tex_skip" : tex_skip, "anchor" : anchor, "spin" : spin, "orient" : orient, "_return_anchor" : _return_anchor, **kwargs})

class _rect_tube_rounding(_Bosl2Base):
    def __init__(self, factor=None, ir=None, r=None, alternative=None, size=None, isize=None, **kwargs):
       super().__init__("_rect_tube_rounding", {"factor" : factor, "ir" : ir, "r" : r, "alternative" : alternative, "size" : size, "isize" : isize, **kwargs})

class rect_tube(_Bosl2Base):
    def __init__(self, h=None, size=None, isize=None, center=None, shift=None, wall=None, size1=None, size2=None, isize1=None, isize2=None, rounding=None, rounding1=None, rounding2=None, irounding=None, irounding1=None, irounding2=None, chamfer=None, chamfer1=None, chamfer2=None, ichamfer=None, ichamfer1=None, ichamfer2=None, anchor=None, spin=None, orient=None, l=None, length=None, height=None, **kwargs):
       super().__init__("rect_tube", {"h" : h, "size" : size, "isize" : isize, "center" : center, "shift" : shift, "wall" : wall, "size1" : size1, "size2" : size2, "isize1" : isize1, "isize2" : isize2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "irounding" : irounding, "irounding1" : irounding1, "irounding2" : irounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "ichamfer" : ichamfer, "ichamfer1" : ichamfer1, "ichamfer2" : ichamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, "length" : length, "height" : height, **kwargs})

class wedge(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("wedge", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class octahedron(_Bosl2Base):
    def __init__(self, size=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("octahedron", {"size" : size, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylinder(_Bosl2Base):
    def __init__(self, h=None, r1=None, r2=None, center=None, r=None, d=None, d1=None, d2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" : center, "r" : r, "d" : d, "d1" : d1, "d2" : d2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _cyl_path(_Bosl2Base):
    def __init__(self, r1=None, r2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, from_end=None, from_end1=None, from_end2=None, teardrop=None, clip_angle=None, n=None, noscale=None, **kwargs):
       super().__init__("_cyl_path", {"r1" : r1, "r2" : r2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "from_end" : from_end, "from_end1" : from_end1, "from_end2" : from_end2, "teardrop" : teardrop, "clip_angle" : clip_angle, "n" : n, "noscale" : noscale, **kwargs})

class cyl(_Bosl2Base):
    def __init__(self, h=None, r=None, center=None, l=None, r1=None, r2=None, d=None, d1=None, d2=None, length=None, height=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, shift=None, teardrop=None, clip_angle=None, from_end=None, from_end1=None, from_end2=None, texture=None, tex_size=None, tex_reps=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_depth=None, tex_samples=None, tex_taper=None, style=None, tex_style=None, extra=None, extra1=None, extra2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cyl", {"h" : h, "r" : r, "center" : center, "l" : l, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "length" : length, "height" : height, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "shift" : shift, "teardrop" : teardrop, "clip_angle" : clip_angle, "from_end" : from_end, "from_end1" : from_end1, "from_end2" : from_end2, "texture" : texture, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_depth" : tex_depth, "tex_samples" : tex_samples, "tex_taper" : tex_taper, "style" : style, "tex_style" : tex_style, "extra" : extra, "extra1" : extra1, "extra2" : extra2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _teardrop_corner(_Bosl2Base):
    def __init__(self, r=None, corner=None, ang=None, **kwargs):
       super().__init__("_teardrop_corner", {"r" : r, "corner" : corner, "ang" : ang, **kwargs})

class _clipped_corner(_Bosl2Base):
    def __init__(self, r=None, corner=None, ang=None, **kwargs):
       super().__init__("_clipped_corner", {"r" : r, "corner" : corner, "ang" : ang, **kwargs})

class xcyl(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("xcyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ycyl(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, height=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ycyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "height" : height, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class zcyl(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("zcyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class tube(_Bosl2Base):
    def __init__(self, h=None, _or=None, ir=None, center=None, od=None, id=None, wall=None, or1=None, or2=None, od1=None, od2=None, ir1=None, ir2=None, id1=None, id2=None, realign=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, orounding1=None, irounding1=None, orounding2=None, irounding2=None, rounding1=None, rounding2=None, rounding=None, ochamfer1=None, ichamfer1=None, ochamfer2=None, ichamfer2=None, chamfer1=None, chamfer2=None, chamfer=None, irounding=None, ichamfer=None, orounding=None, ochamfer=None, teardrop=None, clip_angle=None, shift=None, ifn=None, rounding_fn=None, circum=None, **kwargs):
       super().__init__("tube", {"h" : h, "_or" : _or, "ir" : ir, "center" : center, "od" : od, "id" : id, "wall" : wall, "or1" : or1, "or2" : or2, "od1" : od1, "od2" : od2, "ir1" : ir1, "ir2" : ir2, "id1" : id1, "id2" : id2, "realign" : realign, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, "orounding1" : orounding1, "irounding1" : irounding1, "orounding2" : orounding2, "irounding2" : irounding2, "rounding1" : rounding1, "rounding2" : rounding2, "rounding" : rounding, "ochamfer1" : ochamfer1, "ichamfer1" : ichamfer1, "ochamfer2" : ochamfer2, "ichamfer2" : ichamfer2, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfer" : chamfer, "irounding" : irounding, "ichamfer" : ichamfer, "orounding" : orounding, "ochamfer" : ochamfer, "teardrop" : teardrop, "clip_angle" : clip_angle, "shift" : shift, "ifn" : ifn, "rounding_fn" : rounding_fn, "circum" : circum, **kwargs})

class pie_slice(_Bosl2Base):
    def __init__(self, h=None, r=None, ang=None, center=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pie_slice", {"h" : h, "r" : r, "ang" : ang, "center" : center, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sphere(_Bosl2Base):
    def __init__(self, r=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sphere", {"r" : r, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _subsample_triangle(_Bosl2Base):
    def __init__(self, p=None, N=None, **kwargs):
       super().__init__("_subsample_triangle", {"p" : p, "N" : N, **kwargs})

class _dual_vertices(_Bosl2Base):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("_dual_vertices", {"vnf" : vnf, **kwargs})

class spheroid(_Bosl2Base):
    def __init__(self, r=None, style=None, d=None, circum=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spheroid", {"r" : r, "style" : style, "d" : d, "circum" : circum, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class torus(_Bosl2Base):
    def __init__(self, r_maj=None, r_min=None, center=None, d_maj=None, d_min=None, _or=None, od=None, ir=None, id=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("torus", {"r_maj" : r_maj, "r_min" : r_min, "center" : center, "d_maj" : d_maj, "d_min" : d_min, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class teardrop(_Bosl2Base):
    def __init__(self, h=None, r=None, ang=None, cap_h=None, r1=None, r2=None, d=None, d1=None, d2=None, cap_h1=None, cap_h2=None, chamfer=None, chamfer1=None, chamfer2=None, circum=None, realign=None, bot_corner1=None, bot_corner2=None, bot_corner=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("teardrop", {"h" : h, "r" : r, "ang" : ang, "cap_h" : cap_h, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "cap_h1" : cap_h1, "cap_h2" : cap_h2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "circum" : circum, "realign" : realign, "bot_corner1" : bot_corner1, "bot_corner2" : bot_corner2, "bot_corner" : bot_corner, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class onion(_Bosl2Base):
    def __init__(self, r=None, ang=None, cap_h=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("onion", {"r" : r, "ang" : ang, "cap_h" : cap_h, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _cut_interp(_Bosl2Base):
    def __init__(self, pathcut=None, path=None, data=None, **kwargs):
       super().__init__("_cut_interp", {"pathcut" : pathcut, "path" : path, "data" : data, **kwargs})

class fillet(_Bosl2Base):
    def __init__(self, l=None, r=None, ang=None, r1=None, r2=None, d=None, d1=None, d2=None, excess=None, anchor=None, spin=None, orient=None, h=None, height=None, length=None, **kwargs):
       super().__init__("fillet", {"l" : l, "r" : r, "ang" : ang, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "excess" : excess, "anchor" : anchor, "spin" : spin, "orient" : orient, "h" : h, "height" : height, "length" : length, **kwargs})

class plot3d(_Bosl2Base):
    def __init__(self, f=None, x=None, y=None, zclip=None, zspan=None, base=None, anchor=None, orient=None, spin=None, atype=None, cp=None, style=None, **kwargs):
       super().__init__("plot3d", {"f" : f, "x" : x, "y" : y, "zclip" : zclip, "zspan" : zspan, "base" : base, "anchor" : anchor, "orient" : orient, "spin" : spin, "atype" : atype, "cp" : cp, "style" : style, **kwargs})

class plot_revolution(_Bosl2Base):
    def __init__(self, f=None, angle=None, z=None, arclength=None, path=None, rclip=None, rspan=None, horiz=None, r1=None, r2=None, r=None, d1=None, d2=None, d=None, anchor=None, orient=None, spin=None, atype=None, cp=None, style=None, reverse=None, **kwargs):
       super().__init__("plot_revolution", {"f" : f, "angle" : angle, "z" : z, "arclength" : arclength, "path" : path, "rclip" : rclip, "rspan" : rspan, "horiz" : horiz, "r1" : r1, "r2" : r2, "r" : r, "d1" : d1, "d2" : d2, "d" : d, "anchor" : anchor, "orient" : orient, "spin" : spin, "atype" : atype, "cp" : cp, "style" : style, "reverse" : reverse, **kwargs})

class heightfield(_Bosl2Base):
    def __init__(self, data=None, size=None, bottom=None, maxz=None, xrange=None, yrange=None, style=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("heightfield", {"data" : data, "size" : size, "bottom" : bottom, "maxz" : maxz, "xrange" : xrange, "yrange" : yrange, "style" : style, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylindrical_heightfield(_Bosl2Base):
    def __init__(self, data=None, l=None, r=None, base=None, transpose=None, aspect=None, style=None, maxh=None, xrange=None, yrange=None, r1=None, r2=None, d=None, d1=None, d2=None, h=None, height=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylindrical_heightfield", {"data" : data, "l" : l, "r" : r, "base" : base, "transpose" : transpose, "aspect" : aspect, "style" : style, "maxh" : maxh, "xrange" : xrange, "yrange" : yrange, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "h" : h, "height" : height, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cube(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cube", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cuboid(_Bosl2Base):
    def __init__(self, size=None, p1=None, p2=None, chamfer=None, rounding=None, edges=None, _except=None, except_edges=None, trimcorners=None, teardrop=None, clip_angle=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cuboid", {"size" : size, "p1" : p1, "p2" : p2, "chamfer" : chamfer, "rounding" : rounding, "edges" : edges, "_except" : _except, "except_edges" : except_edges, "trimcorners" : trimcorners, "teardrop" : teardrop, "clip_angle" : clip_angle, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class prismoid(_Bosl2Base):
    def __init__(self, size1=None, size2=None, h=None, shift=None, xang=None, yang=None, rounding=None, rounding1=None, rounding2=None, chamfer=None, chamfer1=None, chamfer2=None, l=None, height=None, length=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("prismoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "xang" : xang, "yang" : yang, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "l" : l, "height" : height, "length" : length, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class regular_prism(_Bosl2Base):
    def __init__(self, n=None, h=None, r=None, center=None, l=None, length=None, height=None, r1=None, r2=None, ir=None, ir1=None, ir2=None, _or=None, or1=None, or2=None, side=None, side1=None, side2=None, d=None, d1=None, d2=None, id=None, id1=None, id2=None, od=None, od1=None, od2=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, realign=None, shift=None, teardrop=None, clip_angle=None, from_end=None, from_end1=None, from_end2=None, texture=None, tex_size=None, tex_reps=None, tex_inset=None, tex_rot=None, tex_depth=None, tex_samples=None, tex_taper=None, style=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("regular_prism", {"n" : n, "h" : h, "r" : r, "center" : center, "l" : l, "length" : length, "height" : height, "r1" : r1, "r2" : r2, "ir" : ir, "ir1" : ir1, "ir2" : ir2, "_or" : _or, "or1" : or1, "or2" : or2, "side" : side, "side1" : side1, "side2" : side2, "d" : d, "d1" : d1, "d2" : d2, "id" : id, "id1" : id1, "id2" : id2, "od" : od, "od1" : od1, "od2" : od2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "realign" : realign, "shift" : shift, "teardrop" : teardrop, "clip_angle" : clip_angle, "from_end" : from_end, "from_end1" : from_end1, "from_end2" : from_end2, "texture" : texture, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "tex_samples" : tex_samples, "tex_taper" : tex_taper, "style" : style, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class textured_tile(_Bosl2Base):
    def __init__(self, texture=None, size=None, ysize=None, height=None, w1=None, w2=None, ang=None, h=None, shift=None, tex_size=None, tex_reps=None, tex_inset=None, tex_rot=None, tex_depth=None, diff=None, tex_extra=None, tex_skip=None, style=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("textured_tile", {"texture" : texture, "size" : size, "ysize" : ysize, "height" : height, "w1" : w1, "w2" : w2, "ang" : ang, "h" : h, "shift" : shift, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "diff" : diff, "tex_extra" : tex_extra, "tex_skip" : tex_skip, "style" : style, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rect_tube(_Bosl2Base):
    def __init__(self, h=None, size=None, isize=None, center=None, shift=None, wall=None, size1=None, size2=None, isize1=None, isize2=None, rounding=None, rounding1=None, rounding2=None, irounding=None, irounding1=None, irounding2=None, chamfer=None, chamfer1=None, chamfer2=None, ichamfer=None, ichamfer1=None, ichamfer2=None, anchor=None, spin=None, orient=None, l=None, length=None, height=None, **kwargs):
       super().__init__("rect_tube", {"h" : h, "size" : size, "isize" : isize, "center" : center, "shift" : shift, "wall" : wall, "size1" : size1, "size2" : size2, "isize1" : isize1, "isize2" : isize2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "irounding" : irounding, "irounding1" : irounding1, "irounding2" : irounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "ichamfer" : ichamfer, "ichamfer1" : ichamfer1, "ichamfer2" : ichamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, "length" : length, "height" : height, **kwargs})

class wedge(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("wedge", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class octahedron(_Bosl2Base):
    def __init__(self, size=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("octahedron", {"size" : size, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylinder(_Bosl2Base):
    def __init__(self, h=None, r1=None, r2=None, center=None, r=None, d=None, d1=None, d2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" : center, "r" : r, "d" : d, "d1" : d1, "d2" : d2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cyl(_Bosl2Base):
    def __init__(self, h=None, r=None, center=None, l=None, r1=None, r2=None, d=None, d1=None, d2=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, shift=None, teardrop=None, clip_angle=None, from_end=None, from_end1=None, from_end2=None, texture=None, tex_size=None, tex_reps=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_depth=None, tex_samples=None, length=None, height=None, tex_taper=None, style=None, tex_style=None, extra=None, extra1=None, extra2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cyl", {"h" : h, "r" : r, "center" : center, "l" : l, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "shift" : shift, "teardrop" : teardrop, "clip_angle" : clip_angle, "from_end" : from_end, "from_end1" : from_end1, "from_end2" : from_end2, "texture" : texture, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_depth" : tex_depth, "tex_samples" : tex_samples, "length" : length, "height" : height, "tex_taper" : tex_taper, "style" : style, "tex_style" : tex_style, "extra" : extra, "extra1" : extra1, "extra2" : extra2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class xcyl(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("xcyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ycyl(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, height=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ycyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "height" : height, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class zcyl(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("zcyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class tube(_Bosl2Base):
    def __init__(self, h=None, _or=None, ir=None, center=None, od=None, id=None, wall=None, or1=None, or2=None, od1=None, od2=None, ir1=None, ir2=None, id1=None, id2=None, realign=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, orounding1=None, irounding1=None, orounding2=None, irounding2=None, rounding1=None, rounding2=None, rounding=None, ochamfer1=None, ichamfer1=None, ochamfer2=None, ichamfer2=None, chamfer1=None, chamfer2=None, chamfer=None, irounding=None, ichamfer=None, orounding=None, ochamfer=None, teardrop=None, clip_angle=None, shift=None, ifn=None, rounding_fn=None, circum=None, **kwargs):
       super().__init__("tube", {"h" : h, "_or" : _or, "ir" : ir, "center" : center, "od" : od, "id" : id, "wall" : wall, "or1" : or1, "or2" : or2, "od1" : od1, "od2" : od2, "ir1" : ir1, "ir2" : ir2, "id1" : id1, "id2" : id2, "realign" : realign, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, "orounding1" : orounding1, "irounding1" : irounding1, "orounding2" : orounding2, "irounding2" : irounding2, "rounding1" : rounding1, "rounding2" : rounding2, "rounding" : rounding, "ochamfer1" : ochamfer1, "ichamfer1" : ichamfer1, "ochamfer2" : ochamfer2, "ichamfer2" : ichamfer2, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfer" : chamfer, "irounding" : irounding, "ichamfer" : ichamfer, "orounding" : orounding, "ochamfer" : ochamfer, "teardrop" : teardrop, "clip_angle" : clip_angle, "shift" : shift, "ifn" : ifn, "rounding_fn" : rounding_fn, "circum" : circum, **kwargs})

class pie_slice(_Bosl2Base):
    def __init__(self, h=None, r=None, ang=None, center=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pie_slice", {"h" : h, "r" : r, "ang" : ang, "center" : center, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sphere(_Bosl2Base):
    def __init__(self, r=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sphere", {"r" : r, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class spheroid(_Bosl2Base):
    def __init__(self, r=None, style=None, d=None, circum=None, dual=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spheroid", {"r" : r, "style" : style, "d" : d, "circum" : circum, "dual" : dual, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class torus(_Bosl2Base):
    def __init__(self, r_maj=None, r_min=None, center=None, d_maj=None, d_min=None, _or=None, od=None, ir=None, id=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("torus", {"r_maj" : r_maj, "r_min" : r_min, "center" : center, "d_maj" : d_maj, "d_min" : d_min, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class teardrop(_Bosl2Base):
    def __init__(self, h=None, r=None, ang=None, cap_h=None, r1=None, r2=None, d=None, d1=None, d2=None, cap_h1=None, cap_h2=None, l=None, length=None, height=None, circum=None, realign=None, chamfer=None, chamfer1=None, chamfer2=None, anchor=None, spin=None, orient=None, bot_corner1=None, bot_corner2=None, bot_corner=None, **kwargs):
       super().__init__("teardrop", {"h" : h, "r" : r, "ang" : ang, "cap_h" : cap_h, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "cap_h1" : cap_h1, "cap_h2" : cap_h2, "l" : l, "length" : length, "height" : height, "circum" : circum, "realign" : realign, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, "bot_corner1" : bot_corner1, "bot_corner2" : bot_corner2, "bot_corner" : bot_corner, **kwargs})

class onion(_Bosl2Base):
    def __init__(self, r=None, ang=None, cap_h=None, d=None, circum=None, realign=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("onion", {"r" : r, "ang" : ang, "cap_h" : cap_h, "d" : d, "circum" : circum, "realign" : realign, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class text3d(_Bosl2Base):
    def __init__(self, text=None, h=None, size=None, font=None, spacing=None, direction=None, language=None, script=None, height=None, thickness=None, atype=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("text3d", {"text" : text, "h" : h, "size" : size, "font" : font, "spacing" : spacing, "direction" : direction, "language" : language, "script" : script, "height" : height, "thickness" : thickness, "atype" : atype, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class path_text(_Bosl2Base):
    def __init__(self, path=None, text=None, font=None, size=None, thickness=None, lettersize=None, offset=None, reverse=None, normal=None, top=None, center=None, textmetrics=None, kern=None, height=None, h=None, valign=None, language=None, script=None, **kwargs):
       super().__init__("path_text", {"path" : path, "text" : text, "font" : font, "size" : size, "thickness" : thickness, "lettersize" : lettersize, "offset" : offset, "reverse" : reverse, "normal" : normal, "top" : top, "center" : center, "textmetrics" : textmetrics, "kern" : kern, "height" : height, "h" : h, "valign" : valign, "language" : language, "script" : script, **kwargs})

class interior_fillet(_Bosl2Base):
    def __init__(self, l=None, r=None, ang=None, overlap=None, d=None, length=None, h=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("interior_fillet", {"l" : l, "r" : r, "ang" : ang, "overlap" : overlap, "d" : d, "length" : length, "h" : h, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class fillet(_Bosl2Base):
    def __init__(self, l=None, r=None, ang=None, r1=None, r2=None, excess=None, d1=None, d2=None, d=None, length=None, h=None, height=None, anchor=None, spin=None, orient=None, rounding=None, rounding1=None, rounding2=None, chamfer=None, chamfer1=None, chamfer2=None, **kwargs):
       super().__init__("fillet", {"l" : l, "r" : r, "ang" : ang, "r1" : r1, "r2" : r2, "excess" : excess, "d1" : d1, "d2" : d2, "d" : d, "length" : length, "h" : h, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, **kwargs})

class plot3d(_Bosl2Base):
    def __init__(self, f=None, x=None, y=None, zclip=None, zspan=None, base=None, anchor=None, orient=None, spin=None, atype=None, cp=None, convexity=None, style=None, **kwargs):
       super().__init__("plot3d", {"f" : f, "x" : x, "y" : y, "zclip" : zclip, "zspan" : zspan, "base" : base, "anchor" : anchor, "orient" : orient, "spin" : spin, "atype" : atype, "cp" : cp, "convexity" : convexity, "style" : style, **kwargs})

class plot_revolution(_Bosl2Base):
    def __init__(self, f=None, angle=None, z=None, arclength=None, path=None, rclip=None, rspan=None, horiz=None, r1=None, r2=None, r=None, d1=None, d2=None, d=None, convexity=None, anchor=None, orient=None, spin=None, atype=None, cp=None, style=None, reverse=None, **kwargs):
       super().__init__("plot_revolution", {"f" : f, "angle" : angle, "z" : z, "arclength" : arclength, "path" : path, "rclip" : rclip, "rspan" : rspan, "horiz" : horiz, "r1" : r1, "r2" : r2, "r" : r, "d1" : d1, "d2" : d2, "d" : d, "convexity" : convexity, "anchor" : anchor, "orient" : orient, "spin" : spin, "atype" : atype, "cp" : cp, "style" : style, "reverse" : reverse, **kwargs})

class heightfield(_Bosl2Base):
    def __init__(self, data=None, size=None, bottom=None, maxz=None, xrange=None, yrange=None, style=None, convexity=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("heightfield", {"data" : data, "size" : size, "bottom" : bottom, "maxz" : maxz, "xrange" : xrange, "yrange" : yrange, "style" : style, "convexity" : convexity, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylindrical_heightfield(_Bosl2Base):
    def __init__(self, data=None, l=None, r=None, base=None, transpose=None, aspect=None, style=None, convexity=None, xrange=None, yrange=None, maxh=None, r1=None, r2=None, d=None, d1=None, d2=None, h=None, height=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylindrical_heightfield", {"data" : data, "l" : l, "r" : r, "base" : base, "transpose" : transpose, "aspect" : aspect, "style" : style, "convexity" : convexity, "xrange" : xrange, "yrange" : yrange, "maxh" : maxh, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "h" : h, "height" : height, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ruler(_Bosl2Base):
    def __init__(self, length=None, width=None, thickness=None, depth=None, labels=None, pipscale=None, maxscale=None, colors=None, alpha=None, unit=None, inch=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ruler", {"length" : length, "width" : width, "thickness" : thickness, "depth" : depth, "labels" : labels, "pipscale" : pipscale, "maxscale" : maxscale, "colors" : colors, "alpha" : alpha, "unit" : unit, "inch" : inch, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

