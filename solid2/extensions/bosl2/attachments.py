from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/attachments.scad'}", False)

_tags = _OpenSCADConstant('_tags')
_tag = _OpenSCADConstant('_tag')
_save_tag = _OpenSCADConstant('_save_tag')
_tag_prefix = _OpenSCADConstant('_tag_prefix')
_overlap = _OpenSCADConstant('_overlap')
_color = _OpenSCADConstant('_color')
_save_color = _OpenSCADConstant('_save_color')
_anchor_override = _OpenSCADConstant('_anchor_override')
_attach_to = _OpenSCADConstant('_attach_to')
_attach_anchor = _OpenSCADConstant('_attach_anchor')
_attach_alignment = _OpenSCADConstant('_attach_alignment')
_parent_anchor = _OpenSCADConstant('_parent_anchor')
_parent_spin = _OpenSCADConstant('_parent_spin')
_parent_orient = _OpenSCADConstant('_parent_orient')
_parent_size = _OpenSCADConstant('_parent_size')
_parent_geom = _OpenSCADConstant('_parent_geom')
_attach_inside = _OpenSCADConstant('_attach_inside')
_edge_angle = _OpenSCADConstant('_edge_angle')
_edge_length = _OpenSCADConstant('_edge_length')
_tags_shown = _OpenSCADConstant('_tags_shown')
_tags_hidden = _OpenSCADConstant('_tags_hidden')
_ghost_this = _OpenSCADConstant('_ghost_this')
_ghost = _OpenSCADConstant('_ghost')
_ghosting = _OpenSCADConstant('_ghosting')
_highlight_this = _OpenSCADConstant('_highlight_this')
_highlight = _OpenSCADConstant('_highlight')
_ANCHOR_TYPES = _OpenSCADConstant('_ANCHOR_TYPES')
EDGES_NONE = _OpenSCADConstant('EDGES_NONE')
EDGES_ALL = _OpenSCADConstant('EDGES_ALL')
EDGE_OFFSETS = _OpenSCADConstant('EDGE_OFFSETS')
CORNERS_NONE = _OpenSCADConstant('CORNERS_NONE')
CORNERS_ALL = _OpenSCADConstant('CORNERS_ALL')
CORNER_OFFSETS = _OpenSCADConstant('CORNER_OFFSETS')
class _quant_anch(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("_quant_anch", {"x" : x, **kwargs})

class _make_anchor_legal(_Bosl2Base):
    def __init__(self, anchor=None, geom=None, **kwargs):
       super().__init__("_make_anchor_legal", {"anchor" : anchor, "geom" : geom, **kwargs})

class _is_geometry(_Bosl2Base):
    def __init__(self, entry=None, **kwargs):
       super().__init__("_is_geometry", {"entry" : entry, **kwargs})

class reorient(_Bosl2Base):
    def __init__(self, anchor=None, spin=None, orient=None, size=None, size2=None, shift=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, h=None, vnf=None, path=None, region=None, extent=None, offset=None, cp=None, anchors=None, two_d=None, axis=None, override=None, geom=None, p=None, **kwargs):
       super().__init__("reorient", {"anchor" : anchor, "spin" : spin, "orient" : orient, "size" : size, "size2" : size2, "shift" : shift, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "h" : h, "vnf" : vnf, "path" : path, "region" : region, "extent" : extent, "offset" : offset, "cp" : cp, "anchors" : anchors, "two_d" : two_d, "axis" : axis, "override" : override, "geom" : geom, "p" : p, **kwargs})

class named_anchor(_Bosl2Base):
    def __init__(self, name=None, pos=None, orient=None, spin=None, rot=None, flip=None, info=None, **kwargs):
       super().__init__("named_anchor", {"name" : name, "pos" : pos, "orient" : orient, "spin" : spin, "rot" : rot, "flip" : flip, "info" : info, **kwargs})

class attach_geom(_Bosl2Base):
    def __init__(self, size=None, size2=None, shift=None, scale=None, twist=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, h=None, vnf=None, region=None, extent=None, cp=None, offset=None, anchors=None, two_d=None, axis=None, override=None, **kwargs):
       super().__init__("attach_geom", {"size" : size, "size2" : size2, "shift" : shift, "scale" : scale, "twist" : twist, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "h" : h, "vnf" : vnf, "region" : region, "extent" : extent, "cp" : cp, "offset" : offset, "anchors" : anchors, "two_d" : two_d, "axis" : axis, "override" : override, **kwargs})

class define_part(_Bosl2Base):
    def __init__(self, name=None, geom=None, inside=None, T=None, **kwargs):
       super().__init__("define_part", {"name" : name, "geom" : geom, "inside" : inside, "T" : T, **kwargs})

class _attach_geom_2d(_Bosl2Base):
    def __init__(self, geom=None, **kwargs):
       super().__init__("_attach_geom_2d", {"geom" : geom, **kwargs})

class _attach_geom_size(_Bosl2Base):
    def __init__(self, geom=None, **kwargs):
       super().__init__("_attach_geom_size", {"geom" : geom, **kwargs})

class _attach_geom_edge_path(_Bosl2Base):
    def __init__(self, geom=None, edge=None, **kwargs):
       super().__init__("_attach_geom_edge_path", {"geom" : geom, "edge" : edge, **kwargs})

class _attach_transform(_Bosl2Base):
    def __init__(self, anchor=None, spin=None, orient=None, geom=None, p=None, **kwargs):
       super().__init__("_attach_transform", {"anchor" : anchor, "spin" : spin, "orient" : orient, "geom" : geom, "p" : p, **kwargs})

class _get_cp(_Bosl2Base):
    def __init__(self, geom=None, **kwargs):
       super().__init__("_get_cp", {"geom" : geom, **kwargs})

class _get_cp(_Bosl2Base):
    def __init__(self, geom=None, **kwargs):
       super().__init__("_get_cp", {"geom" : geom, **kwargs})

class _three_edge_corner_dir(_Bosl2Base):
    def __init__(self, facevecs=None, edges=None, **kwargs):
       super().__init__("_three_edge_corner_dir", {"facevecs" : facevecs, "edges" : edges, **kwargs})

class _find_anchor(_Bosl2Base):
    def __init__(self, anchor=None, geom=None, **kwargs):
       super().__init__("_find_anchor", {"anchor" : anchor, "geom" : geom, **kwargs})

class _is_shown(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("_is_shown", {**kwargs})

class _standard_anchors(_Bosl2Base):
    def __init__(self, two_d=None, **kwargs):
       super().__init__("_standard_anchors", {"two_d" : two_d, **kwargs})

class _edges_vec_txt(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("_edges_vec_txt", {"x" : x, **kwargs})

class _edges_text(_Bosl2Base):
    def __init__(self, edges=None, **kwargs):
       super().__init__("_edges_text", {"edges" : edges, **kwargs})

class _is_edge_array(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("_is_edge_array", {"x" : x, **kwargs})

class _edge_set(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("_edge_set", {"v" : v, **kwargs})

class _normalize_edges(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("_normalize_edges", {"v" : v, **kwargs})

class _edges(_Bosl2Base):
    def __init__(self, v=None, _except=None, **kwargs):
       super().__init__("_edges", {"v" : v, "_except" : _except, **kwargs})

class _is_corner_array(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("_is_corner_array", {"x" : x, **kwargs})

class _normalize_corners(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("_normalize_corners", {"v" : v, **kwargs})

class _corner_set(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("_corner_set", {"v" : v, **kwargs})

class _corners(_Bosl2Base):
    def __init__(self, v=None, _except=None, **kwargs):
       super().__init__("_corners", {"v" : v, "_except" : _except, **kwargs})

class _corner_edges(_Bosl2Base):
    def __init__(self, edges=None, v=None, **kwargs):
       super().__init__("_corner_edges", {"edges" : edges, "v" : v, **kwargs})

class _corner_edge_count(_Bosl2Base):
    def __init__(self, edges=None, v=None, **kwargs):
       super().__init__("_corner_edge_count", {"edges" : edges, "v" : v, **kwargs})

class _corners_text(_Bosl2Base):
    def __init__(self, corners=None, **kwargs):
       super().__init__("_corners_text", {"corners" : corners, **kwargs})

class _force_rot(_Bosl2Base):
    def __init__(self, T=None, **kwargs):
       super().__init__("_force_rot", {"T" : T, **kwargs})

class _local_struct_val(_Bosl2Base):
    def __init__(self, struct=None, key=None, **kwargs):
       super().__init__("_local_struct_val", {"struct" : struct, "key" : key, **kwargs})

class _force_anchor_2d(_Bosl2Base):
    def __init__(self, anchor=None, **kwargs):
       super().__init__("_force_anchor_2d", {"anchor" : anchor, **kwargs})

class _compute_spin(_Bosl2Base):
    def __init__(self, anchor_dir=None, spin_dir=None, **kwargs):
       super().__init__("_compute_spin", {"anchor_dir" : anchor_dir, "spin_dir" : spin_dir, **kwargs})

class _canonical_edge(_Bosl2Base):
    def __init__(self, edge=None, **kwargs):
       super().__init__("_canonical_edge", {"edge" : edge, **kwargs})

class parent(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("parent", {**kwargs})

class parent_part(_Bosl2Base):
    def __init__(self, name=None, **kwargs):
       super().__init__("parent_part", {"name" : name, **kwargs})

class desc_point(_Bosl2Base):
    def __init__(self, desc=None, p=None, anchor=None, **kwargs):
       super().__init__("desc_point", {"desc" : desc, "p" : p, "anchor" : anchor, **kwargs})

class desc_dir(_Bosl2Base):
    def __init__(self, desc=None, dir=None, anchor=None, **kwargs):
       super().__init__("desc_dir", {"desc" : desc, "dir" : dir, "anchor" : anchor, **kwargs})

class desc_attach(_Bosl2Base):
    def __init__(self, desc=None, anchor=None, p=None, reverse=None, **kwargs):
       super().__init__("desc_attach", {"desc" : desc, "anchor" : anchor, "p" : p, "reverse" : reverse, **kwargs})

class desc_dist(_Bosl2Base):
    def __init__(self, desc1=None, anchor1=None, desc2=None, anchor2=None, **kwargs):
       super().__init__("desc_dist", {"desc1" : desc1, "anchor1" : anchor1, "desc2" : desc2, "anchor2" : anchor2, **kwargs})

class transform_desc(_Bosl2Base):
    def __init__(self, T=None, desc=None, **kwargs):
       super().__init__("transform_desc", {"T" : T, "desc" : desc, **kwargs})

class is_description(_Bosl2Base):
    def __init__(self, desc=None, **kwargs):
       super().__init__("is_description", {"desc" : desc, **kwargs})

class position(_Bosl2Base):
    def __init__(self, at=None, _from=None, **kwargs):
       super().__init__("position", {"at" : at, "_from" : _from, **kwargs})

class orient(_Bosl2Base):
    def __init__(self, anchor=None, spin=None, **kwargs):
       super().__init__("orient", {"anchor" : anchor, "spin" : spin, **kwargs})

class align(_Bosl2Base):
    def __init__(self, anchor=None, align=None, inside=None, inset=None, shiftout=None, overlap=None, **kwargs):
       super().__init__("align", {"anchor" : anchor, "align" : align, "inside" : inside, "inset" : inset, "shiftout" : shiftout, "overlap" : overlap, **kwargs})

class attach(_Bosl2Base):
    def __init__(self, parent=None, child=None, overlap=None, align=None, spin=None, norot=None, inset=None, shiftout=None, inside=None, _from=None, to=None, **kwargs):
       super().__init__("attach", {"parent" : parent, "child" : child, "overlap" : overlap, "align" : align, "spin" : spin, "norot" : norot, "inset" : inset, "shiftout" : shiftout, "inside" : inside, "_from" : _from, "to" : to, **kwargs})

class attach_part(_Bosl2Base):
    def __init__(self, name=None, **kwargs):
       super().__init__("attach_part", {"name" : name, **kwargs})

class tag(_Bosl2Base):
    def __init__(self, tag=None, **kwargs):
       super().__init__("tag", {"tag" : tag, **kwargs})

class tag_this(_Bosl2Base):
    def __init__(self, tag=None, **kwargs):
       super().__init__("tag_this", {"tag" : tag, **kwargs})

class force_tag(_Bosl2Base):
    def __init__(self, tag=None, **kwargs):
       super().__init__("force_tag", {"tag" : tag, **kwargs})

class default_tag(_Bosl2Base):
    def __init__(self, tag=None, do_tag=None, **kwargs):
       super().__init__("default_tag", {"tag" : tag, "do_tag" : do_tag, **kwargs})

class tag_scope(_Bosl2Base):
    def __init__(self, scope=None, **kwargs):
       super().__init__("tag_scope", {"scope" : scope, **kwargs})

class diff(_Bosl2Base):
    def __init__(self, remove=None, keep=None, **kwargs):
       super().__init__("diff", {"remove" : remove, "keep" : keep, **kwargs})

class tag_diff(_Bosl2Base):
    def __init__(self, tag=None, remove=None, keep=None, **kwargs):
       super().__init__("tag_diff", {"tag" : tag, "remove" : remove, "keep" : keep, **kwargs})

class intersect(_Bosl2Base):
    def __init__(self, intersect=None, keep=None, **kwargs):
       super().__init__("intersect", {"intersect" : intersect, "keep" : keep, **kwargs})

class tag_intersect(_Bosl2Base):
    def __init__(self, tag=None, intersect=None, keep=None, **kwargs):
       super().__init__("tag_intersect", {"tag" : tag, "intersect" : intersect, "keep" : keep, **kwargs})

class conv_hull(_Bosl2Base):
    def __init__(self, keep=None, **kwargs):
       super().__init__("conv_hull", {"keep" : keep, **kwargs})

class tag_conv_hull(_Bosl2Base):
    def __init__(self, tag=None, keep=None, **kwargs):
       super().__init__("tag_conv_hull", {"tag" : tag, "keep" : keep, **kwargs})

class hide(_Bosl2Base):
    def __init__(self, tags=None, **kwargs):
       super().__init__("hide", {"tags" : tags, **kwargs})

class hide_this(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("hide_this", {**kwargs})

class show_only(_Bosl2Base):
    def __init__(self, tags=None, **kwargs):
       super().__init__("show_only", {"tags" : tags, **kwargs})

class show_all(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("show_all", {**kwargs})

class show_int(_Bosl2Base):
    def __init__(self, tags=None, **kwargs):
       super().__init__("show_int", {"tags" : tags, **kwargs})

class face_mask(_Bosl2Base):
    def __init__(self, faces=None, **kwargs):
       super().__init__("face_mask", {"faces" : faces, **kwargs})

class edge_mask(_Bosl2Base):
    def __init__(self, edges=None, _except=None, **kwargs):
       super().__init__("edge_mask", {"edges" : edges, "_except" : _except, **kwargs})

class corner_mask(_Bosl2Base):
    def __init__(self, corners=None, _except=None, **kwargs):
       super().__init__("corner_mask", {"corners" : corners, "_except" : _except, **kwargs})

class face_profile(_Bosl2Base):
    def __init__(self, faces=None, r=None, d=None, excess=None, convexity=None, **kwargs):
       super().__init__("face_profile", {"faces" : faces, "r" : r, "d" : d, "excess" : excess, "convexity" : convexity, **kwargs})

class edge_profile(_Bosl2Base):
    def __init__(self, edges=None, _except=None, excess=None, convexity=None, **kwargs):
       super().__init__("edge_profile", {"edges" : edges, "_except" : _except, "excess" : excess, "convexity" : convexity, **kwargs})

class edge_profile_asym(_Bosl2Base):
    def __init__(self, edges=None, _except=None, excess=None, convexity=None, flip=None, corner_type=None, size=None, **kwargs):
       super().__init__("edge_profile_asym", {"edges" : edges, "_except" : _except, "excess" : excess, "convexity" : convexity, "flip" : flip, "corner_type" : corner_type, "size" : size, **kwargs})

class corner_profile(_Bosl2Base):
    def __init__(self, corners=None, _except=None, r=None, d=None, convexity=None, **kwargs):
       super().__init__("corner_profile", {"corners" : corners, "_except" : _except, "r" : r, "d" : d, "convexity" : convexity, **kwargs})

class attachable(_Bosl2Base):
    def __init__(self, anchor=None, spin=None, orient=None, size=None, size2=None, shift=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, h=None, vnf=None, path=None, region=None, extent=None, cp=None, offset=None, anchors=None, two_d=None, axis=None, override=None, geom=None, parts=None, expose_tags=None, keep_color=None, **kwargs):
       super().__init__("attachable", {"anchor" : anchor, "spin" : spin, "orient" : orient, "size" : size, "size2" : size2, "shift" : shift, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "h" : h, "vnf" : vnf, "path" : path, "region" : region, "extent" : extent, "cp" : cp, "offset" : offset, "anchors" : anchors, "two_d" : two_d, "axis" : axis, "override" : override, "geom" : geom, "parts" : parts, "expose_tags" : expose_tags, "keep_color" : keep_color, **kwargs})

class _show_highlight(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("_show_highlight", {**kwargs})

class _show_ghost(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("_show_ghost", {**kwargs})

class show_anchors(_Bosl2Base):
    def __init__(self, s=None, std=None, custom=None, **kwargs):
       super().__init__("show_anchors", {"s" : s, "std" : std, "custom" : custom, **kwargs})

class anchor_arrow(_Bosl2Base):
    def __init__(self, s=None, color=None, flag=None, _tag=None, _fn=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("anchor_arrow", {"s" : s, "color" : color, "flag" : flag, "_tag" : _tag, "_fn" : _fn, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class anchor_arrow2d(_Bosl2Base):
    def __init__(self, s=None, color=None, _tag=None, **kwargs):
       super().__init__("anchor_arrow2d", {"s" : s, "color" : color, "_tag" : _tag, **kwargs})

class expose_anchors(_Bosl2Base):
    def __init__(self, opacity=None, **kwargs):
       super().__init__("expose_anchors", {"opacity" : opacity, **kwargs})

class show_transform_list(_Bosl2Base):
    def __init__(self, tlist=None, s=None, **kwargs):
       super().__init__("show_transform_list", {"tlist" : tlist, "s" : s, **kwargs})

class generic_airplane(_Bosl2Base):
    def __init__(self, s=None, **kwargs):
       super().__init__("generic_airplane", {"s" : s, **kwargs})

class frame_ref(_Bosl2Base):
    def __init__(self, s=None, opacity=None, **kwargs):
       super().__init__("frame_ref", {"s" : s, "opacity" : opacity, **kwargs})

class _edges_text3d(_Bosl2Base):
    def __init__(self, txt=None, size=None, **kwargs):
       super().__init__("_edges_text3d", {"txt" : txt, "size" : size, **kwargs})

class _show_edges(_Bosl2Base):
    def __init__(self, edges=None, size=None, text=None, txtsize=None, toplabel=None, **kwargs):
       super().__init__("_show_edges", {"edges" : edges, "size" : size, "text" : text, "txtsize" : txtsize, "toplabel" : toplabel, **kwargs})

class _show_corners(_Bosl2Base):
    def __init__(self, corners=None, size=None, text=None, txtsize=None, toplabel=None, **kwargs):
       super().__init__("_show_corners", {"corners" : corners, "size" : size, "text" : text, "txtsize" : txtsize, "toplabel" : toplabel, **kwargs})

class _show_cube_faces(_Bosl2Base):
    def __init__(self, faces=None, size=None, toplabel=None, botlabel=None, **kwargs):
       super().__init__("_show_cube_faces", {"faces" : faces, "size" : size, "toplabel" : toplabel, "botlabel" : botlabel, **kwargs})

class restore(_Bosl2Base):
    def __init__(self, desc=None, **kwargs):
       super().__init__("restore", {"desc" : desc, **kwargs})

class desc_copies(_Bosl2Base):
    def __init__(self, transforms=None, **kwargs):
       super().__init__("desc_copies", {"transforms" : transforms, **kwargs})

