from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/skin.scad'}", False)

__vnf_no_n_mesg = _OpenSCADConstant('__vnf_no_n_mesg')
_leadin_ogive = _OpenSCADConstant('_leadin_ogive')
_leadin_cut = _OpenSCADConstant('_leadin_cut')
_leadin_sqrt = _OpenSCADConstant('_leadin_sqrt')
_leadin_linear = _OpenSCADConstant('_leadin_linear')
_lead_in_table = _OpenSCADConstant('_lead_in_table')
_MAP_DIAG = _OpenSCADConstant('_MAP_DIAG')
_MAP_LEFT = _OpenSCADConstant('_MAP_LEFT')
_MAP_UP = _OpenSCADConstant('_MAP_UP')
class skin(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, refine=None, method=None, sampling=None, caps=None, closed=None, z=None, style=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("skin", {"profiles" : profiles, "slices" : slices, "refine" : refine, "method" : method, "sampling" : sampling, "caps" : caps, "closed" : closed, "z" : z, "style" : style, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class _make_all_prism_anchors(_Bosl2Base):
    def __init__(self, bot=None, top=None, startind=None, **kwargs):
       super().__init__("_make_all_prism_anchors", {"bot" : bot, "top" : top, "startind" : startind, **kwargs})

class linear_sweep(_Bosl2Base):
    def __init__(self, region=None, height=None, center=None, twist=None, scale=None, shift=None, slices=None, maxseg=None, style=None, caps=None, cp=None, atype=None, h=None, texture=None, tex_size=None, tex_reps=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_depth=None, tex_samples=None, l=None, length=None, anchor=None, spin=None, orient=None, _return_geom=None, **kwargs):
       super().__init__("linear_sweep", {"region" : region, "height" : height, "center" : center, "twist" : twist, "scale" : scale, "shift" : shift, "slices" : slices, "maxseg" : maxseg, "style" : style, "caps" : caps, "cp" : cp, "atype" : atype, "h" : h, "texture" : texture, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_depth" : tex_depth, "tex_samples" : tex_samples, "l" : l, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, "_return_geom" : _return_geom, **kwargs})

class rotate_sweep(_Bosl2Base):
    def __init__(self, shape=None, angle=None, texture=None, tex_size=None, tex_counts=None, tex_reps=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_depth=None, tex_samples=None, tex_aspect=None, pixel_aspect=None, tex_taper=None, shift=None, caps=None, closed=None, style=None, cp=None, atype=None, anchor=None, spin=None, orient=None, start=None, _tex_inhibit_y_slicing=None, **kwargs):
       super().__init__("rotate_sweep", {"shape" : shape, "angle" : angle, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_reps" : tex_reps, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_depth" : tex_depth, "tex_samples" : tex_samples, "tex_aspect" : tex_aspect, "pixel_aspect" : pixel_aspect, "tex_taper" : tex_taper, "shift" : shift, "caps" : caps, "closed" : closed, "style" : style, "cp" : cp, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, "start" : start, "_tex_inhibit_y_slicing" : _tex_inhibit_y_slicing, **kwargs})

class _force_xplus(_Bosl2Base):
    def __init__(self, data=None, **kwargs):
       super().__init__("_force_xplus", {"data" : data, **kwargs})

class _ss_polygon_r(_Bosl2Base):
    def __init__(self, N=None, theta=None, **kwargs):
       super().__init__("_ss_polygon_r", {"N" : N, "theta" : theta, **kwargs})

class spiral_sweep(_Bosl2Base):
    def __init__(self, poly=None, h=None, r=None, turns=None, taper=None, r1=None, r2=None, d=None, d1=None, d2=None, internal=None, lead_in_shape=None, lead_in_shape1=None, lead_in_shape2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, height=None, l=None, length=None, lead_in_sample=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spiral_sweep", {"poly" : poly, "h" : h, "r" : r, "turns" : turns, "taper" : taper, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "internal" : internal, "lead_in_shape" : lead_in_shape, "lead_in_shape1" : lead_in_shape1, "lead_in_shape2" : lead_in_shape2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "height" : height, "l" : l, "length" : length, "lead_in_sample" : lead_in_sample, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class path_sweep(_Bosl2Base):
    def __init__(self, shape=None, path=None, method=None, normal=None, closed=None, twist=None, twist_by_length=None, scale=None, scale_by_length=None, symmetry=None, last_normal=None, tangent=None, uniform=None, relaxed=None, caps=None, style=None, transforms=None, texture=None, tex_reps=None, tex_size=None, tex_samples=None, tex_inset=None, tex_rot=None, tex_depth=None, tex_extra=None, tex_skip=None, anchor=None, cp=None, spin=None, orient=None, atype=None, _return_scales=None, **kwargs):
       super().__init__("path_sweep", {"shape" : shape, "path" : path, "method" : method, "normal" : normal, "closed" : closed, "twist" : twist, "twist_by_length" : twist_by_length, "scale" : scale, "scale_by_length" : scale_by_length, "symmetry" : symmetry, "last_normal" : last_normal, "tangent" : tangent, "uniform" : uniform, "relaxed" : relaxed, "caps" : caps, "style" : style, "transforms" : transforms, "texture" : texture, "tex_reps" : tex_reps, "tex_size" : tex_size, "tex_samples" : tex_samples, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "tex_extra" : tex_extra, "tex_skip" : tex_skip, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, "_return_scales" : _return_scales, **kwargs})

class path_sweep2d(_Bosl2Base):
    def __init__(self, shape=None, path=None, closed=None, caps=None, quality=None, style=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("path_sweep2d", {"shape" : shape, "path" : path, "closed" : closed, "caps" : caps, "quality" : quality, "style" : style, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class _ofs_vmap(_Bosl2Base):
    def __init__(self, ofs=None, closed=None, **kwargs):
       super().__init__("_ofs_vmap", {"ofs" : ofs, "closed" : closed, **kwargs})

class _ofs_face_edge(_Bosl2Base):
    def __init__(self, face=None, firstlen=None, second=None, **kwargs):
       super().__init__("_ofs_face_edge", {"face" : face, "firstlen" : firstlen, "second" : second, **kwargs})

class sweep(_Bosl2Base):
    def __init__(self, shape=None, transforms=None, closed=None, caps=None, style=None, anchor=None, cp=None, spin=None, orient=None, atype=None, texture=None, tex_reps=None, tex_size=None, tex_samples=None, tex_inset=None, tex_rot=None, tex_depth=None, tex_extra=None, tex_skip=None, _closed_for_normals=None, normals=None, **kwargs):
       super().__init__("sweep", {"shape" : shape, "transforms" : transforms, "closed" : closed, "caps" : caps, "style" : style, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, "texture" : texture, "tex_reps" : tex_reps, "tex_size" : tex_size, "tex_samples" : tex_samples, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "tex_extra" : tex_extra, "tex_skip" : tex_skip, "_closed_for_normals" : _closed_for_normals, "normals" : normals, **kwargs})

class _force_int(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("_force_int", {"x" : x, **kwargs})

class _find_ps_dir(_Bosl2Base):
    def __init__(self, frac=None, prevind=None, nextind=None, twist=None, anchor_pos=None, anchor_dir=None, **kwargs):
       super().__init__("_find_ps_dir", {"frac" : frac, "prevind" : prevind, "nextind" : nextind, "twist" : twist, "anchor_pos" : anchor_pos, "anchor_dir" : anchor_dir, **kwargs})

class subdivide_and_slice(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, numpoints=None, method=None, closed=None, **kwargs):
       super().__init__("subdivide_and_slice", {"profiles" : profiles, "slices" : slices, "numpoints" : numpoints, "method" : method, "closed" : closed, **kwargs})

class slice_profiles(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, closed=None, **kwargs):
       super().__init__("slice_profiles", {"profiles" : profiles, "slices" : slices, "closed" : closed, **kwargs})

class _closest_angle(_Bosl2Base):
    def __init__(self, alpha=None, beta=None, **kwargs):
       super().__init__("_closest_angle", {"alpha" : alpha, "beta" : beta, **kwargs})

class _smooth(_Bosl2Base):
    def __init__(self, data=None, len=None, closed=None, angle=None, **kwargs):
       super().__init__("_smooth", {"data" : data, "len" : len, "closed" : closed, "angle" : angle, **kwargs})

class rot_resample(_Bosl2Base):
    def __init__(self, rotlist=None, n=None, twist=None, scale=None, smoothlen=None, long=None, turns=None, closed=None, method=None, **kwargs):
       super().__init__("rot_resample", {"rotlist" : rotlist, "n" : n, "twist" : twist, "scale" : scale, "smoothlen" : smoothlen, "long" : long, "turns" : turns, "closed" : closed, "method" : method, **kwargs})

class _dp_distance_array(_Bosl2Base):
    def __init__(self, small=None, big=None, abort_thresh=None, **kwargs):
       super().__init__("_dp_distance_array", {"small" : small, "big" : big, "abort_thresh" : abort_thresh, **kwargs})

class _dp_distance_row(_Bosl2Base):
    def __init__(self, small=None, big=None, small_ind=None, tdist=None, **kwargs):
       super().__init__("_dp_distance_row", {"small" : small, "big" : big, "small_ind" : small_ind, "tdist" : tdist, **kwargs})

class _dp_extract_map(_Bosl2Base):
    def __init__(self, map=None, **kwargs):
       super().__init__("_dp_extract_map", {"map" : map, **kwargs})

class _skin_distance_match(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, **kwargs):
       super().__init__("_skin_distance_match", {"poly1" : poly1, "poly2" : poly2, **kwargs})

class _skin_aligned_distance_match(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, **kwargs):
       super().__init__("_skin_aligned_distance_match", {"poly1" : poly1, "poly2" : poly2, **kwargs})

class _skin_tangent_match(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, **kwargs):
       super().__init__("_skin_tangent_match", {"poly1" : poly1, "poly2" : poly2, **kwargs})

class _find_one_tangent(_Bosl2Base):
    def __init__(self, curve=None, edge=None, curve_offset=None, closed=None, **kwargs):
       super().__init__("_find_one_tangent", {"curve" : curve, "edge" : edge, "curve_offset" : curve_offset, "closed" : closed, **kwargs})

class associate_vertices(_Bosl2Base):
    def __init__(self, polygons=None, split=None, curpoly=None, **kwargs):
       super().__init__("associate_vertices", {"polygons" : polygons, "split" : split, "curpoly" : curpoly, **kwargs})

class _tex_fn_default(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("_tex_fn_default", {**kwargs})

class texture(_Bosl2Base):
    def __init__(self, tex=None, n=None, border=None, gap=None, roughness=None, inset=None, **kwargs):
       super().__init__("texture", {"tex" : tex, "n" : n, "border" : border, "gap" : gap, "roughness" : roughness, "inset" : inset, **kwargs})

class _get_vnf_tile_edges(_Bosl2Base):
    def __init__(self, texture=None, **kwargs):
       super().__init__("_get_vnf_tile_edges", {"texture" : texture, **kwargs})

class _validate_texture(_Bosl2Base):
    def __init__(self, texture=None, **kwargs):
       super().__init__("_validate_texture", {"texture" : texture, **kwargs})

class _tex_height(_Bosl2Base):
    def __init__(self, scale=None, inset=None, z=None, **kwargs):
       super().__init__("_tex_height", {"scale" : scale, "inset" : inset, "z" : z, **kwargs})

class _get_texture(_Bosl2Base):
    def __init__(self, texture=None, tex_rot=None, **kwargs):
       super().__init__("_get_texture", {"texture" : texture, "tex_rot" : tex_rot, **kwargs})

class _textured_linear_sweep(_Bosl2Base):
    def __init__(self, region=None, texture=None, tex_size=None, h=None, counts=None, inset=None, rot=None, tex_scale=None, twist=None, scale=None, shift=None, style=None, l=None, caps=None, height=None, length=None, samples=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("_textured_linear_sweep", {"region" : region, "texture" : texture, "tex_size" : tex_size, "h" : h, "counts" : counts, "inset" : inset, "rot" : rot, "tex_scale" : tex_scale, "twist" : twist, "scale" : scale, "shift" : shift, "style" : style, "l" : l, "caps" : caps, "height" : height, "length" : length, "samples" : samples, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _tile_edge_path_list(_Bosl2Base):
    def __init__(self, vnf=None, axis=None, maxopen=None, **kwargs):
       super().__init__("_tile_edge_path_list", {"vnf" : vnf, "axis" : axis, "maxopen" : maxopen, **kwargs})

class _textured_revolution(_Bosl2Base):
    def __init__(self, shape=None, texture=None, tex_size=None, tex_scale=None, inset=None, rot=None, shift=None, taper=None, closed=None, angle=None, inhibit_y_slicing=None, tex_aspect=None, pixel_aspect=None, counts=None, samples=None, start=None, tex_extra=None, style=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("_textured_revolution", {"shape" : shape, "texture" : texture, "tex_size" : tex_size, "tex_scale" : tex_scale, "inset" : inset, "rot" : rot, "shift" : shift, "taper" : taper, "closed" : closed, "angle" : angle, "inhibit_y_slicing" : inhibit_y_slicing, "tex_aspect" : tex_aspect, "pixel_aspect" : pixel_aspect, "counts" : counts, "samples" : samples, "start" : start, "tex_extra" : tex_extra, "style" : style, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _textured_point_array(_Bosl2Base):
    def __init__(self, points=None, texture=None, tex_reps=None, tex_size=None, tex_samples=None, tex_inset=None, tex_rot=None, triangulate=None, tex_scaling=None, return_edges=None, col_wrap=None, tex_depth=None, row_wrap=None, caps=None, cap1=None, cap2=None, reverse=None, style=None, tex_extra=None, tex_skip=None, sidecaps=None, sidecap1=None, sidecap2=None, normals=None, **kwargs):
       super().__init__("_textured_point_array", {"points" : points, "texture" : texture, "tex_reps" : tex_reps, "tex_size" : tex_size, "tex_samples" : tex_samples, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "triangulate" : triangulate, "tex_scaling" : tex_scaling, "return_edges" : return_edges, "col_wrap" : col_wrap, "tex_depth" : tex_depth, "row_wrap" : row_wrap, "caps" : caps, "cap1" : cap1, "cap2" : cap2, "reverse" : reverse, "style" : style, "tex_extra" : tex_extra, "tex_skip" : tex_skip, "sidecaps" : sidecaps, "sidecap1" : sidecap1, "sidecap2" : sidecap2, "normals" : normals, **kwargs})

class _resample_point_array(_Bosl2Base):
    def __init__(self, data=None, size=None, col_wrap=None, row_wrap=None, **kwargs):
       super().__init__("_resample_point_array", {"data" : data, "size" : size, "col_wrap" : col_wrap, "row_wrap" : row_wrap, **kwargs})

class skin(_Bosl2Base):
    def __init__(self, profiles=None, slices=None, refine=None, method=None, sampling=None, caps=None, closed=None, z=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("skin", {"profiles" : profiles, "slices" : slices, "refine" : refine, "method" : method, "sampling" : sampling, "caps" : caps, "closed" : closed, "z" : z, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class linear_sweep(_Bosl2Base):
    def __init__(self, region=None, height=None, center=None, twist=None, scale=None, shift=None, slices=None, maxseg=None, style=None, convexity=None, caps=None, texture=None, tex_size=None, tex_reps=None, tex_counts=None, tex_inset=None, tex_rot=None, tex_depth=None, tex_scale=None, tex_samples=None, cp=None, atype=None, h=None, l=None, length=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("linear_sweep", {"region" : region, "height" : height, "center" : center, "twist" : twist, "scale" : scale, "shift" : shift, "slices" : slices, "maxseg" : maxseg, "style" : style, "convexity" : convexity, "caps" : caps, "texture" : texture, "tex_size" : tex_size, "tex_reps" : tex_reps, "tex_counts" : tex_counts, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "tex_scale" : tex_scale, "tex_samples" : tex_samples, "cp" : cp, "atype" : atype, "h" : h, "l" : l, "length" : length, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rotate_sweep(_Bosl2Base):
    def __init__(self, shape=None, angle=None, texture=None, tex_size=None, tex_counts=None, tex_reps=None, tex_inset=None, tex_rot=None, tex_scale=None, tex_depth=None, tex_samples=None, tex_taper=None, shift=None, style=None, caps=None, closed=None, tex_extra=None, tex_aspect=None, pixel_aspect=None, cp=None, convexity=None, atype=None, anchor=None, spin=None, orient=None, start=None, _tex_inhibit_y_slicing=None, **kwargs):
       super().__init__("rotate_sweep", {"shape" : shape, "angle" : angle, "texture" : texture, "tex_size" : tex_size, "tex_counts" : tex_counts, "tex_reps" : tex_reps, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_scale" : tex_scale, "tex_depth" : tex_depth, "tex_samples" : tex_samples, "tex_taper" : tex_taper, "shift" : shift, "style" : style, "caps" : caps, "closed" : closed, "tex_extra" : tex_extra, "tex_aspect" : tex_aspect, "pixel_aspect" : pixel_aspect, "cp" : cp, "convexity" : convexity, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, "start" : start, "_tex_inhibit_y_slicing" : _tex_inhibit_y_slicing, **kwargs})

class spiral_sweep(_Bosl2Base):
    def __init__(self, poly=None, h=None, r=None, turns=None, taper=None, r1=None, r2=None, d=None, d1=None, d2=None, internal=None, lead_in_shape=None, lead_in_shape1=None, lead_in_shape2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, height=None, l=None, length=None, lead_in_sample=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spiral_sweep", {"poly" : poly, "h" : h, "r" : r, "turns" : turns, "taper" : taper, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "internal" : internal, "lead_in_shape" : lead_in_shape, "lead_in_shape1" : lead_in_shape1, "lead_in_shape2" : lead_in_shape2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "height" : height, "l" : l, "length" : length, "lead_in_sample" : lead_in_sample, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class path_sweep(_Bosl2Base):
    def __init__(self, shape=None, path=None, method=None, normal=None, closed=None, twist=None, twist_by_length=None, scale=None, scale_by_length=None, symmetry=None, last_normal=None, tangent=None, uniform=None, relaxed=None, caps=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, profiles=None, width=None, texture=None, tex_reps=None, tex_size=None, tex_samples=None, tex_inset=None, tex_rot=None, tex_depth=None, tex_extra=None, tex_skip=None, **kwargs):
       super().__init__("path_sweep", {"shape" : shape, "path" : path, "method" : method, "normal" : normal, "closed" : closed, "twist" : twist, "twist_by_length" : twist_by_length, "scale" : scale, "scale_by_length" : scale_by_length, "symmetry" : symmetry, "last_normal" : last_normal, "tangent" : tangent, "uniform" : uniform, "relaxed" : relaxed, "caps" : caps, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, "profiles" : profiles, "width" : width, "texture" : texture, "tex_reps" : tex_reps, "tex_size" : tex_size, "tex_samples" : tex_samples, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "tex_extra" : tex_extra, "tex_skip" : tex_skip, **kwargs})

class path_sweep2d(_Bosl2Base):
    def __init__(self, profile=None, path=None, closed=None, caps=None, quality=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("path_sweep2d", {"profile" : profile, "path" : path, "closed" : closed, "caps" : caps, "quality" : quality, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class sweep(_Bosl2Base):
    def __init__(self, shape=None, transforms=None, closed=None, caps=None, style=None, convexity=None, anchor=None, cp=None, spin=None, orient=None, atype=None, texture=None, tex_reps=None, tex_size=None, tex_samples=None, tex_inset=None, tex_rot=None, tex_depth=None, tex_extra=None, tex_skip=None, normals=None, **kwargs):
       super().__init__("sweep", {"shape" : shape, "transforms" : transforms, "closed" : closed, "caps" : caps, "style" : style, "convexity" : convexity, "anchor" : anchor, "cp" : cp, "spin" : spin, "orient" : orient, "atype" : atype, "texture" : texture, "tex_reps" : tex_reps, "tex_size" : tex_size, "tex_samples" : tex_samples, "tex_inset" : tex_inset, "tex_rot" : tex_rot, "tex_depth" : tex_depth, "tex_extra" : tex_extra, "tex_skip" : tex_skip, "normals" : normals, **kwargs})

class sweep_attach(_Bosl2Base):
    def __init__(self, parent=None, child=None, frac=None, idx=None, pathlen=None, spin=None, overlap=None, atype=None, cp=None, **kwargs):
       super().__init__("sweep_attach", {"parent" : parent, "child" : child, "frac" : frac, "idx" : idx, "pathlen" : pathlen, "spin" : spin, "overlap" : overlap, "atype" : atype, "cp" : cp, **kwargs})

class _textured_revolution(_Bosl2Base):
    def __init__(self, shape=None, texture=None, tex_size=None, tex_scale=None, inset=None, rot=None, shift=None, taper=None, closed=None, angle=None, style=None, atype=None, tex_aspect=None, pixel_aspect=None, inhibit_y_slicing=None, tex_extra=None, convexity=None, counts=None, samples=None, start=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("_textured_revolution", {"shape" : shape, "texture" : texture, "tex_size" : tex_size, "tex_scale" : tex_scale, "inset" : inset, "rot" : rot, "shift" : shift, "taper" : taper, "closed" : closed, "angle" : angle, "style" : style, "atype" : atype, "tex_aspect" : tex_aspect, "pixel_aspect" : pixel_aspect, "inhibit_y_slicing" : inhibit_y_slicing, "tex_extra" : tex_extra, "convexity" : convexity, "counts" : counts, "samples" : samples, "start" : start, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

