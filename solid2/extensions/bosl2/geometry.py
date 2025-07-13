from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/geometry.scad'}", False)

class is_point_on_line(_Bosl2Base):
    def __init__(self, point=None, line=None, bounded=None, eps=None, **kwargs):
       super().__init__("is_point_on_line", {"point" : point, "line" : line, "bounded" : bounded, "eps" : eps, **kwargs})

class _is_point_on_line(_Bosl2Base):
    def __init__(self, point=None, line=None, bounded=None, eps=None, **kwargs):
       super().__init__("_is_point_on_line", {"point" : point, "line" : line, "bounded" : bounded, "eps" : eps, **kwargs})

class _dist2line(_Bosl2Base):
    def __init__(self, d=None, n=None, **kwargs):
       super().__init__("_dist2line", {"d" : d, "n" : n, **kwargs})

class _valid_line(_Bosl2Base):
    def __init__(self, line=None, dim=None, eps=None, **kwargs):
       super().__init__("_valid_line", {"line" : line, "dim" : dim, "eps" : eps, **kwargs})

class _valid_plane(_Bosl2Base):
    def __init__(self, p=None, eps=None, **kwargs):
       super().__init__("_valid_plane", {"p" : p, "eps" : eps, **kwargs})

class _is_at_left(_Bosl2Base):
    def __init__(self, pt=None, line=None, eps=None, **kwargs):
       super().__init__("_is_at_left", {"pt" : pt, "line" : line, "eps" : eps, **kwargs})

class _degenerate_tri(_Bosl2Base):
    def __init__(self, tri=None, eps=None, **kwargs):
       super().__init__("_degenerate_tri", {"tri" : tri, "eps" : eps, **kwargs})

class _tri_class(_Bosl2Base):
    def __init__(self, tri=None, eps=None, **kwargs):
       super().__init__("_tri_class", {"tri" : tri, "eps" : eps, **kwargs})

class _pt_in_tri(_Bosl2Base):
    def __init__(self, point=None, tri=None, eps=None, **kwargs):
       super().__init__("_pt_in_tri", {"point" : point, "tri" : tri, "eps" : eps, **kwargs})

class _point_left_of_line2d(_Bosl2Base):
    def __init__(self, point=None, line=None, eps=None, **kwargs):
       super().__init__("_point_left_of_line2d", {"point" : point, "line" : line, "eps" : eps, **kwargs})

class is_collinear(_Bosl2Base):
    def __init__(self, a=None, b=None, c=None, eps=None, **kwargs):
       super().__init__("is_collinear", {"a" : a, "b" : b, "c" : c, "eps" : eps, **kwargs})

class point_line_distance(_Bosl2Base):
    def __init__(self, pt=None, line=None, bounded=None, **kwargs):
       super().__init__("point_line_distance", {"pt" : pt, "line" : line, "bounded" : bounded, **kwargs})

class segment_distance(_Bosl2Base):
    def __init__(self, seg1=None, seg2=None, eps=None, **kwargs):
       super().__init__("segment_distance", {"seg1" : seg1, "seg2" : seg2, "eps" : eps, **kwargs})

class line_normal(_Bosl2Base):
    def __init__(self, p1=None, p2=None, **kwargs):
       super().__init__("line_normal", {"p1" : p1, "p2" : p2, **kwargs})

class _general_line_intersection(_Bosl2Base):
    def __init__(self, s1=None, s2=None, eps=None, **kwargs):
       super().__init__("_general_line_intersection", {"s1" : s1, "s2" : s2, "eps" : eps, **kwargs})

class line_intersection(_Bosl2Base):
    def __init__(self, line1=None, line2=None, bounded1=None, bounded2=None, bounded=None, eps=None, **kwargs):
       super().__init__("line_intersection", {"line1" : line1, "line2" : line2, "bounded1" : bounded1, "bounded2" : bounded2, "bounded" : bounded, "eps" : eps, **kwargs})

class line_closest_point(_Bosl2Base):
    def __init__(self, line=None, pt=None, bounded=None, **kwargs):
       super().__init__("line_closest_point", {"line" : line, "pt" : pt, "bounded" : bounded, **kwargs})

class _line_greatest_distance(_Bosl2Base):
    def __init__(self, points=None, line=None, **kwargs):
       super().__init__("_line_greatest_distance", {"points" : points, "line" : line, **kwargs})

class line_from_points(_Bosl2Base):
    def __init__(self, points=None, check_collinear=None, eps=None, fast=None, **kwargs):
       super().__init__("line_from_points", {"points" : points, "check_collinear" : check_collinear, "eps" : eps, "fast" : fast, **kwargs})

class is_coplanar(_Bosl2Base):
    def __init__(self, points=None, eps=None, **kwargs):
       super().__init__("is_coplanar", {"points" : points, "eps" : eps, **kwargs})

class plane3pt(_Bosl2Base):
    def __init__(self, p1=None, p2=None, p3=None, **kwargs):
       super().__init__("plane3pt", {"p1" : p1, "p2" : p2, "p3" : p3, **kwargs})

class plane3pt_indexed(_Bosl2Base):
    def __init__(self, points=None, i1=None, i2=None, i3=None, **kwargs):
       super().__init__("plane3pt_indexed", {"points" : points, "i1" : i1, "i2" : i2, "i3" : i3, **kwargs})

class plane_from_normal(_Bosl2Base):
    def __init__(self, normal=None, pt=None, **kwargs):
       super().__init__("plane_from_normal", {"normal" : normal, "pt" : pt, **kwargs})

class _eigenvals_symm_3(_Bosl2Base):
    def __init__(self, M=None, **kwargs):
       super().__init__("_eigenvals_symm_3", {"M" : M, **kwargs})

class _eigenvec_symm_3(_Bosl2Base):
    def __init__(self, M=None, evals=None, i=None, **kwargs):
       super().__init__("_eigenvec_symm_3", {"M" : M, "evals" : evals, "i" : i, **kwargs})

class _covariance_evec_eval(_Bosl2Base):
    def __init__(self, points=None, eigenvalue_id=None, **kwargs):
       super().__init__("_covariance_evec_eval", {"points" : points, "eigenvalue_id" : eigenvalue_id, **kwargs})

class plane_from_points(_Bosl2Base):
    def __init__(self, points=None, check_coplanar=None, eps=None, fast=None, **kwargs):
       super().__init__("plane_from_points", {"points" : points, "check_coplanar" : check_coplanar, "eps" : eps, "fast" : fast, **kwargs})

class plane_from_polygon(_Bosl2Base):
    def __init__(self, poly=None, check_coplanar=None, eps=None, fast=None, **kwargs):
       super().__init__("plane_from_polygon", {"poly" : poly, "check_coplanar" : check_coplanar, "eps" : eps, "fast" : fast, **kwargs})

class plane_normal(_Bosl2Base):
    def __init__(self, plane=None, **kwargs):
       super().__init__("plane_normal", {"plane" : plane, **kwargs})

class plane_offset(_Bosl2Base):
    def __init__(self, plane=None, **kwargs):
       super().__init__("plane_offset", {"plane" : plane, **kwargs})

class _general_plane_line_intersection(_Bosl2Base):
    def __init__(self, plane=None, line=None, eps=None, **kwargs):
       super().__init__("_general_plane_line_intersection", {"plane" : plane, "line" : line, "eps" : eps, **kwargs})

class _normalize_plane(_Bosl2Base):
    def __init__(self, plane=None, **kwargs):
       super().__init__("_normalize_plane", {"plane" : plane, **kwargs})

class plane_line_intersection(_Bosl2Base):
    def __init__(self, plane=None, line=None, bounded=None, eps=None, **kwargs):
       super().__init__("plane_line_intersection", {"plane" : plane, "line" : line, "bounded" : bounded, "eps" : eps, **kwargs})

class plane_intersection(_Bosl2Base):
    def __init__(self, plane1=None, plane2=None, plane3=None, **kwargs):
       super().__init__("plane_intersection", {"plane1" : plane1, "plane2" : plane2, "plane3" : plane3, **kwargs})

class plane_line_angle(_Bosl2Base):
    def __init__(self, plane=None, line=None, **kwargs):
       super().__init__("plane_line_angle", {"plane" : plane, "line" : line, **kwargs})

class plane_closest_point(_Bosl2Base):
    def __init__(self, plane=None, points=None, **kwargs):
       super().__init__("plane_closest_point", {"plane" : plane, "points" : points, **kwargs})

class point_plane_distance(_Bosl2Base):
    def __init__(self, plane=None, point=None, **kwargs):
       super().__init__("point_plane_distance", {"plane" : plane, "point" : point, **kwargs})

class _pointlist_greatest_distance(_Bosl2Base):
    def __init__(self, points=None, plane=None, **kwargs):
       super().__init__("_pointlist_greatest_distance", {"points" : points, "plane" : plane, **kwargs})

class are_points_on_plane(_Bosl2Base):
    def __init__(self, points=None, plane=None, eps=None, **kwargs):
       super().__init__("are_points_on_plane", {"points" : points, "plane" : plane, "eps" : eps, **kwargs})

class _is_point_above_plane(_Bosl2Base):
    def __init__(self, plane=None, point=None, **kwargs):
       super().__init__("_is_point_above_plane", {"plane" : plane, "point" : point, **kwargs})

class circle_line_intersection(_Bosl2Base):
    def __init__(self, r=None, cp=None, line=None, bounded=None, d=None, eps=None, **kwargs):
       super().__init__("circle_line_intersection", {"r" : r, "cp" : cp, "line" : line, "bounded" : bounded, "d" : d, "eps" : eps, **kwargs})

class _circle_or_sphere_line_intersection(_Bosl2Base):
    def __init__(self, r=None, cp=None, line=None, bounded=None, d=None, eps=None, **kwargs):
       super().__init__("_circle_or_sphere_line_intersection", {"r" : r, "cp" : cp, "line" : line, "bounded" : bounded, "d" : d, "eps" : eps, **kwargs})

class circle_circle_intersection(_Bosl2Base):
    def __init__(self, r1=None, cp1=None, r2=None, cp2=None, eps=None, d1=None, d2=None, **kwargs):
       super().__init__("circle_circle_intersection", {"r1" : r1, "cp1" : cp1, "r2" : r2, "cp2" : cp2, "eps" : eps, "d1" : d1, "d2" : d2, **kwargs})

class circle_2tangents(_Bosl2Base):
    def __init__(self, r=None, pt1=None, pt2=None, pt3=None, tangents=None, d=None, **kwargs):
       super().__init__("circle_2tangents", {"r" : r, "pt1" : pt1, "pt2" : pt2, "pt3" : pt3, "tangents" : tangents, "d" : d, **kwargs})

class circle_3points(_Bosl2Base):
    def __init__(self, pt1=None, pt2=None, pt3=None, **kwargs):
       super().__init__("circle_3points", {"pt1" : pt1, "pt2" : pt2, "pt3" : pt3, **kwargs})

class circle_point_tangents(_Bosl2Base):
    def __init__(self, r=None, cp=None, pt=None, d=None, **kwargs):
       super().__init__("circle_point_tangents", {"r" : r, "cp" : cp, "pt" : pt, "d" : d, **kwargs})

class circle_circle_tangents(_Bosl2Base):
    def __init__(self, r1=None, cp1=None, r2=None, cp2=None, d1=None, d2=None, **kwargs):
       super().__init__("circle_circle_tangents", {"r1" : r1, "cp1" : cp1, "r2" : r2, "cp2" : cp2, "d1" : d1, "d2" : d2, **kwargs})

class _noncollinear_triple(_Bosl2Base):
    def __init__(self, points=None, error=None, eps=None, **kwargs):
       super().__init__("_noncollinear_triple", {"points" : points, "error" : error, "eps" : eps, **kwargs})

class sphere_line_intersection(_Bosl2Base):
    def __init__(self, r=None, cp=None, line=None, bounded=None, d=None, eps=None, **kwargs):
       super().__init__("sphere_line_intersection", {"r" : r, "cp" : cp, "line" : line, "bounded" : bounded, "d" : d, "eps" : eps, **kwargs})

class polygon_area(_Bosl2Base):
    def __init__(self, poly=None, signed=None, **kwargs):
       super().__init__("polygon_area", {"poly" : poly, "signed" : signed, **kwargs})

class centroid(_Bosl2Base):
    def __init__(self, object=None, eps=None, **kwargs):
       super().__init__("centroid", {"object" : object, "eps" : eps, **kwargs})

class _region_centroid(_Bosl2Base):
    def __init__(self, region=None, eps=None, **kwargs):
       super().__init__("_region_centroid", {"region" : region, "eps" : eps, **kwargs})

class _polygon_centroid(_Bosl2Base):
    def __init__(self, poly=None, eps=None, **kwargs):
       super().__init__("_polygon_centroid", {"poly" : poly, "eps" : eps, **kwargs})

class polygon_normal(_Bosl2Base):
    def __init__(self, poly=None, **kwargs):
       super().__init__("polygon_normal", {"poly" : poly, **kwargs})

class _point_above_below_segment(_Bosl2Base):
    def __init__(self, point=None, edge=None, **kwargs):
       super().__init__("_point_above_below_segment", {"point" : point, "edge" : edge, **kwargs})

class point_in_polygon(_Bosl2Base):
    def __init__(self, point=None, poly=None, nonzero=None, eps=None, **kwargs):
       super().__init__("point_in_polygon", {"point" : point, "poly" : poly, "nonzero" : nonzero, "eps" : eps, **kwargs})

class polygon_line_intersection(_Bosl2Base):
    def __init__(self, poly=None, line=None, bounded=None, nonzero=None, eps=None, **kwargs):
       super().__init__("polygon_line_intersection", {"poly" : poly, "line" : line, "bounded" : bounded, "nonzero" : nonzero, "eps" : eps, **kwargs})

class _merge_segments(_Bosl2Base):
    def __init__(self, insegs=None, outsegs=None, eps=None, i=None, **kwargs):
       super().__init__("_merge_segments", {"insegs" : insegs, "outsegs" : outsegs, "eps" : eps, "i" : i, **kwargs})

class polygon_triangulate(_Bosl2Base):
    def __init__(self, poly=None, ind=None, error=None, eps=None, **kwargs):
       super().__init__("polygon_triangulate", {"poly" : poly, "ind" : ind, "error" : error, "eps" : eps, **kwargs})

class _triangulate(_Bosl2Base):
    def __init__(self, poly=None, ind=None, error=None, eps=None, tris=None, **kwargs):
       super().__init__("_triangulate", {"poly" : poly, "ind" : ind, "error" : error, "eps" : eps, "tris" : tris, **kwargs})

class _get_ear(_Bosl2Base):
    def __init__(self, poly=None, ind=None, eps=None, _i=None, **kwargs):
       super().__init__("_get_ear", {"poly" : poly, "ind" : ind, "eps" : eps, "_i" : _i, **kwargs})

class _none_inside(_Bosl2Base):
    def __init__(self, idxs=None, poly=None, p0=None, p1=None, p2=None, eps=None, i=None, **kwargs):
       super().__init__("_none_inside", {"idxs" : idxs, "poly" : poly, "p0" : p0, "p1" : p1, "p2" : p2, "eps" : eps, "i" : i, **kwargs})

class is_polygon_clockwise(_Bosl2Base):
    def __init__(self, poly=None, **kwargs):
       super().__init__("is_polygon_clockwise", {"poly" : poly, **kwargs})

class clockwise_polygon(_Bosl2Base):
    def __init__(self, poly=None, **kwargs):
       super().__init__("clockwise_polygon", {"poly" : poly, **kwargs})

class ccw_polygon(_Bosl2Base):
    def __init__(self, poly=None, **kwargs):
       super().__init__("ccw_polygon", {"poly" : poly, **kwargs})

class reverse_polygon(_Bosl2Base):
    def __init__(self, poly=None, **kwargs):
       super().__init__("reverse_polygon", {"poly" : poly, **kwargs})

class reindex_polygon(_Bosl2Base):
    def __init__(self, reference=None, poly=None, return_error=None, **kwargs):
       super().__init__("reindex_polygon", {"reference" : reference, "poly" : poly, "return_error" : return_error, **kwargs})

class align_polygon(_Bosl2Base):
    def __init__(self, reference=None, poly=None, angles=None, cp=None, trans=None, return_ind=None, **kwargs):
       super().__init__("align_polygon", {"reference" : reference, "poly" : poly, "angles" : angles, "cp" : cp, "trans" : trans, "return_ind" : return_ind, **kwargs})

class are_polygons_equal(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, eps=None, **kwargs):
       super().__init__("are_polygons_equal", {"poly1" : poly1, "poly2" : poly2, "eps" : eps, **kwargs})

class _are_polygons_equal(_Bosl2Base):
    def __init__(self, poly1=None, poly2=None, eps=None, st=None, **kwargs):
       super().__init__("_are_polygons_equal", {"poly1" : poly1, "poly2" : poly2, "eps" : eps, "st" : st, **kwargs})

class _is_polygon_in_list(_Bosl2Base):
    def __init__(self, poly=None, polys=None, **kwargs):
       super().__init__("_is_polygon_in_list", {"poly" : poly, "polys" : polys, **kwargs})

class ___is_polygon_in_list(_Bosl2Base):
    def __init__(self, poly=None, polys=None, i=None, **kwargs):
       super().__init__("___is_polygon_in_list", {"poly" : poly, "polys" : polys, "i" : i, **kwargs})

class hull(_Bosl2Base):
    def __init__(self, points=None, **kwargs):
       super().__init__("hull", {"points" : points, **kwargs})

class _backtracking(_Bosl2Base):
    def __init__(self, i=None, points=None, h=None, t=None, m=None, all=None, **kwargs):
       super().__init__("_backtracking", {"i" : i, "points" : points, "h" : h, "t" : t, "m" : m, "all" : all, **kwargs})

class _is_cw(_Bosl2Base):
    def __init__(self, a=None, b=None, c=None, all=None, **kwargs):
       super().__init__("_is_cw", {"a" : a, "b" : b, "c" : c, "all" : all, **kwargs})

class hull2d_path(_Bosl2Base):
    def __init__(self, points=None, all=None, **kwargs):
       super().__init__("hull2d_path", {"points" : points, "all" : all, **kwargs})

class _hull_collinear(_Bosl2Base):
    def __init__(self, points=None, **kwargs):
       super().__init__("_hull_collinear", {"points" : points, **kwargs})

class hull3d_faces(_Bosl2Base):
    def __init__(self, points=None, **kwargs):
       super().__init__("hull3d_faces", {"points" : points, **kwargs})

class _hull3d_iterative(_Bosl2Base):
    def __init__(self, points=None, triangles=None, planes=None, remaining=None, _i=None, **kwargs):
       super().__init__("_hull3d_iterative", {"points" : points, "triangles" : triangles, "planes" : planes, "remaining" : remaining, "_i" : _i, **kwargs})

class _remove_internal_edges(_Bosl2Base):
    def __init__(self, halfedges=None, **kwargs):
       super().__init__("_remove_internal_edges", {"halfedges" : halfedges, **kwargs})

class _find_first_noncoplanar(_Bosl2Base):
    def __init__(self, plane=None, points=None, i=None, **kwargs):
       super().__init__("_find_first_noncoplanar", {"plane" : plane, "points" : points, "i" : i, **kwargs})

class is_polygon_convex(_Bosl2Base):
    def __init__(self, poly=None, eps=None, **kwargs):
       super().__init__("is_polygon_convex", {"poly" : poly, "eps" : eps, **kwargs})

class convex_distance(_Bosl2Base):
    def __init__(self, points1=None, points2=None, eps=None, **kwargs):
       super().__init__("convex_distance", {"points1" : points1, "points2" : points2, "eps" : eps, **kwargs})

class _GJK_distance(_Bosl2Base):
    def __init__(self, points1=None, points2=None, eps=None, lbd=None, d=None, simplex=None, **kwargs):
       super().__init__("_GJK_distance", {"points1" : points1, "points2" : points2, "eps" : eps, "lbd" : lbd, "d" : d, "simplex" : simplex, **kwargs})

class convex_collision(_Bosl2Base):
    def __init__(self, points1=None, points2=None, eps=None, **kwargs):
       super().__init__("convex_collision", {"points1" : points1, "points2" : points2, "eps" : eps, **kwargs})

class _GJK_collide(_Bosl2Base):
    def __init__(self, points1=None, points2=None, d=None, simplex=None, eps=None, **kwargs):
       super().__init__("_GJK_collide", {"points1" : points1, "points2" : points2, "d" : d, "simplex" : simplex, "eps" : eps, **kwargs})

class _closest_simplex(_Bosl2Base):
    def __init__(self, s=None, eps=None, **kwargs):
       super().__init__("_closest_simplex", {"s" : s, "eps" : eps, **kwargs})

class _closest_s1(_Bosl2Base):
    def __init__(self, s=None, eps=None, **kwargs):
       super().__init__("_closest_s1", {"s" : s, "eps" : eps, **kwargs})

class _closest_s2(_Bosl2Base):
    def __init__(self, s=None, eps=None, **kwargs):
       super().__init__("_closest_s2", {"s" : s, "eps" : eps, **kwargs})

class _closest_s3(_Bosl2Base):
    def __init__(self, s=None, eps=None, **kwargs):
       super().__init__("_closest_s3", {"s" : s, "eps" : eps, **kwargs})

class _tri_normal(_Bosl2Base):
    def __init__(self, tri=None, **kwargs):
       super().__init__("_tri_normal", {"tri" : tri, **kwargs})

class _support_diff(_Bosl2Base):
    def __init__(self, p1=None, p2=None, d=None, **kwargs):
       super().__init__("_support_diff", {"p1" : p1, "p2" : p2, "d" : d, **kwargs})

class rot_decode(_Bosl2Base):
    def __init__(self, M=None, long=None, **kwargs):
       super().__init__("rot_decode", {"M" : M, "long" : long, **kwargs})

class show_plane(_Bosl2Base):
    def __init__(self, plane=None, size=None, offset=None, **kwargs):
       super().__init__("show_plane", {"plane" : plane, "size" : size, "offset" : offset, **kwargs})

class hull_points(_Bosl2Base):
    def __init__(self, points=None, fast=None, **kwargs):
       super().__init__("hull_points", {"points" : points, "fast" : fast, **kwargs})

