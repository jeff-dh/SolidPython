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

class octahedron(_Bosl2Base):
    def __init__(self, size=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("octahedron", {"size" : size, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _rect_tube_rounding(_Bosl2Base):
    def __init__(self, factor=None, ir=None, r=None, alternative=None, size=None, isize=None, **kwargs):
       super().__init__("_rect_tube_rounding", {"factor" : factor, "ir" : ir, "r" : r, "alternative" : alternative, "size" : size, "isize" : isize, **kwargs})

class rect_tube(_Bosl2Base):
    def __init__(self, h=None, size=None, isize=None, center=None, shift=None, wall=None, size1=None, size2=None, isize1=None, isize2=None, rounding=None, rounding1=None, rounding2=None, irounding=None, irounding1=None, irounding2=None, chamfer=None, chamfer1=None, chamfer2=None, ichamfer=None, ichamfer1=None, ichamfer2=None, anchor=None, spin=None, orient=None, l=None, length=None, height=None, **kwargs):
       super().__init__("rect_tube", {"h" : h, "size" : size, "isize" : isize, "center" : center, "shift" : shift, "wall" : wall, "size1" : size1, "size2" : size2, "isize1" : isize1, "isize2" : isize2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "irounding" : irounding, "irounding1" : irounding1, "irounding2" : irounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "ichamfer" : ichamfer, "ichamfer1" : ichamfer1, "ichamfer2" : ichamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, "length" : length, "height" : height, **kwargs})

class wedge(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("wedge", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylinder(_Bosl2Base):
    def __init__(self, h=None, r1=None, r2=None, center=None, r=None, d=None, d1=None, d2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" : center, "r" : r, "d" : d, "d1" : d1, "d2" : d2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cyl(_Bosl2Base):
    def __init__(self, h=None, r=None, center=None, l=None, r1=None, r2=None, d=None, d1=None, d2=None, length=None, height=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, shift=None, teardrop=None, from_end=None, from_end1=None, from_end2=None, texture=None, tex_size=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_samples=None, tex_taper=None, tex_style=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cyl", {"h" : h, "r" : r, "center" : center, "l" : l, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "length" : length, "height" : height, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "shift" : shift, "teardrop" : teardrop, "from_end" : from_end, "from_end1" : from_end1, "from_end2" : from_end2, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_samples" : tex_samples, "tex_taper" : tex_taper, "tex_style" : tex_style, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _teardrop_corner(_Bosl2Base):
    def __init__(self, r=None, corner=None, ang=None, **kwargs):
       super().__init__("_teardrop_corner", {"r" : r, "corner" : corner, "ang" : ang, **kwargs})

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
    def __init__(self, h=None, _or=None, ir=None, center=None, od=None, id=None, wall=None, or1=None, or2=None, od1=None, od2=None, ir1=None, ir2=None, id1=None, id2=None, realign=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("tube", {"h" : h, "_or" : _or, "ir" : ir, "center" : center, "od" : od, "id" : id, "wall" : wall, "or1" : or1, "or2" : or2, "od1" : od1, "od2" : od2, "ir1" : ir1, "ir2" : ir2, "id1" : id1, "id2" : id2, "realign" : realign, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

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
    def __init__(self, h=None, r=None, ang=None, cap_h=None, r1=None, r2=None, d=None, d1=None, d2=None, cap_h1=None, cap_h2=None, chamfer=None, chamfer1=None, chamfer2=None, circum=None, realign=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("teardrop", {"h" : h, "r" : r, "ang" : ang, "cap_h" : cap_h, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "cap_h1" : cap_h1, "cap_h2" : cap_h2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "circum" : circum, "realign" : realign, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class onion(_Bosl2Base):
    def __init__(self, r=None, ang=None, cap_h=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("onion", {"r" : r, "ang" : ang, "cap_h" : cap_h, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _cut_interp(_Bosl2Base):
    def __init__(self, pathcut=None, path=None, data=None, **kwargs):
       super().__init__("_cut_interp", {"pathcut" : pathcut, "path" : path, "data" : data, **kwargs})

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
    def __init__(self, size=None, p1=None, p2=None, chamfer=None, rounding=None, edges=None, _except=None, except_edges=None, trimcorners=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cuboid", {"size" : size, "p1" : p1, "p2" : p2, "chamfer" : chamfer, "rounding" : rounding, "edges" : edges, "_except" : _except, "except_edges" : except_edges, "trimcorners" : trimcorners, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class prismoid(_Bosl2Base):
    def __init__(self, size1=None, size2=None, h=None, shift=None, xang=None, yang=None, rounding=None, rounding1=None, rounding2=None, chamfer=None, chamfer1=None, chamfer2=None, l=None, height=None, length=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("prismoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "xang" : xang, "yang" : yang, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "l" : l, "height" : height, "length" : length, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class octahedron(_Bosl2Base):
    def __init__(self, size=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("octahedron", {"size" : size, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rect_tube(_Bosl2Base):
    def __init__(self, h=None, size=None, isize=None, center=None, shift=None, wall=None, size1=None, size2=None, isize1=None, isize2=None, rounding=None, rounding1=None, rounding2=None, irounding=None, irounding1=None, irounding2=None, chamfer=None, chamfer1=None, chamfer2=None, ichamfer=None, ichamfer1=None, ichamfer2=None, anchor=None, spin=None, orient=None, l=None, length=None, height=None, **kwargs):
       super().__init__("rect_tube", {"h" : h, "size" : size, "isize" : isize, "center" : center, "shift" : shift, "wall" : wall, "size1" : size1, "size2" : size2, "isize1" : isize1, "isize2" : isize2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "irounding" : irounding, "irounding1" : irounding1, "irounding2" : irounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "ichamfer" : ichamfer, "ichamfer1" : ichamfer1, "ichamfer2" : ichamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, "length" : length, "height" : height, **kwargs})

class wedge(_Bosl2Base):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("wedge", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylinder(_Bosl2Base):
    def __init__(self, h=None, r1=None, r2=None, center=None, r=None, d=None, d1=None, d2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" : center, "r" : r, "d" : d, "d1" : d1, "d2" : d2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cyl(_Bosl2Base):
    def __init__(self, h=None, r=None, center=None, l=None, r1=None, r2=None, d=None, d1=None, d2=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, shift=None, teardrop=None, from_end=None, from_end1=None, from_end2=None, texture=None, tex_size=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_samples=None, length=None, height=None, tex_taper=None, tex_style=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cyl", {"h" : h, "r" : r, "center" : center, "l" : l, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "shift" : shift, "teardrop" : teardrop, "from_end" : from_end, "from_end1" : from_end1, "from_end2" : from_end2, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_samples" : tex_samples, "length" : length, "height" : height, "tex_taper" : tex_taper, "tex_style" : tex_style, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

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
    def __init__(self, h=None, _or=None, ir=None, center=None, od=None, id=None, wall=None, or1=None, or2=None, od1=None, od2=None, ir1=None, ir2=None, id1=None, id2=None, realign=None, l=None, length=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("tube", {"h" : h, "_or" : _or, "ir" : ir, "center" : center, "od" : od, "id" : id, "wall" : wall, "or1" : or1, "or2" : or2, "od1" : od1, "od2" : od2, "ir1" : ir1, "ir2" : ir2, "id1" : id1, "id2" : id2, "realign" : realign, "l" : l, "length" : length, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

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
    def __init__(self, h=None, r=None, ang=None, cap_h=None, r1=None, r2=None, d=None, d1=None, d2=None, cap_h1=None, cap_h2=None, l=None, length=None, height=None, circum=None, realign=None, chamfer=None, chamfer1=None, chamfer2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("teardrop", {"h" : h, "r" : r, "ang" : ang, "cap_h" : cap_h, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "cap_h1" : cap_h1, "cap_h2" : cap_h2, "l" : l, "length" : length, "height" : height, "circum" : circum, "realign" : realign, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

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
    def __init__(self, l=None, r=None, ang=None, overlap=None, d=None, length=None, h=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("fillet", {"l" : l, "r" : r, "ang" : ang, "overlap" : overlap, "d" : d, "length" : length, "h" : h, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class heightfield(_Bosl2Base):
    def __init__(self, data=None, size=None, bottom=None, maxz=None, xrange=None, yrange=None, style=None, convexity=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("heightfield", {"data" : data, "size" : size, "bottom" : bottom, "maxz" : maxz, "xrange" : xrange, "yrange" : yrange, "style" : style, "convexity" : convexity, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylindrical_heightfield(_Bosl2Base):
    def __init__(self, data=None, l=None, r=None, base=None, transpose=None, aspect=None, style=None, convexity=None, xrange=None, yrange=None, maxh=None, r1=None, r2=None, d=None, d1=None, d2=None, h=None, height=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylindrical_heightfield", {"data" : data, "l" : l, "r" : r, "base" : base, "transpose" : transpose, "aspect" : aspect, "style" : style, "convexity" : convexity, "xrange" : xrange, "yrange" : yrange, "maxh" : maxh, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "h" : h, "height" : height, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ruler(_Bosl2Base):
    def __init__(self, length=None, width=None, thickness=None, depth=None, labels=None, pipscale=None, maxscale=None, colors=None, alpha=None, unit=None, inch=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ruler", {"length" : length, "width" : width, "thickness" : thickness, "depth" : depth, "labels" : labels, "pipscale" : pipscale, "maxscale" : maxscale, "colors" : colors, "alpha" : alpha, "unit" : unit, "inch" : inch, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

