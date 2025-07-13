from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/regions.scad'}", False)

class is_region(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_region", {"x" : x, **kwargs})

class is_valid_region(_Bosl2Base):
    def __init__(self, region=None, eps=None, **kwargs):
       super().__init__("is_valid_region", {"region" : region, "eps" : eps, **kwargs})

class _polygon_crosses_region(_Bosl2Base):
    def __init__(self, region=None, poly=None, eps=None, **kwargs):
       super().__init__("_polygon_crosses_region", {"region" : region, "poly" : poly, "eps" : eps, **kwargs})

class is_region_simple(_Bosl2Base):
    def __init__(self, region=None, eps=None, **kwargs):
       super().__init__("is_region_simple", {"region" : region, "eps" : eps, **kwargs})

class make_region(_Bosl2Base):
    def __init__(self, polys=None, nonzero=None, eps=None, **kwargs):
       super().__init__("make_region", {"polys" : polys, "nonzero" : nonzero, "eps" : eps, **kwargs})

class force_region(_Bosl2Base):
    def __init__(self, poly=None, **kwargs):
       super().__init__("force_region", {"poly" : poly, **kwargs})

class point_in_region(_Bosl2Base):
    def __init__(self, point=None, region=None, eps=None, **kwargs):
       super().__init__("point_in_region", {"point" : point, "region" : region, "eps" : eps, **kwargs})

class _point_in_region(_Bosl2Base):
    def __init__(self, point=None, region=None, eps=None, i=None, cnt=None, **kwargs):
       super().__init__("_point_in_region", {"point" : point, "region" : region, "eps" : eps, "i" : i, "cnt" : cnt, **kwargs})

class region_area(_Bosl2Base):
    def __init__(self, region=None, **kwargs):
       super().__init__("region_area", {"region" : region, **kwargs})

class _clockwise_region(_Bosl2Base):
    def __init__(self, r=None, **kwargs):
       super().__init__("_clockwise_region", {"r" : r, **kwargs})

class are_regions_equal(_Bosl2Base):
    def __init__(self, region1=None, region2=None, either_winding=None, **kwargs):
       super().__init__("are_regions_equal", {"region1" : region1, "region2" : region2, "either_winding" : either_winding, **kwargs})

class __are_regions_equal(_Bosl2Base):
    def __init__(self, region1=None, region2=None, i=None, **kwargs):
       super().__init__("__are_regions_equal", {"region1" : region1, "region2" : region2, "i" : i, **kwargs})

class _region_region_intersections(_Bosl2Base):
    def __init__(self, region1=None, region2=None, closed1=None, closed2=None, eps=None, **kwargs):
       super().__init__("_region_region_intersections", {"region1" : region1, "region2" : region2, "closed1" : closed1, "closed2" : closed2, "eps" : eps, **kwargs})

class split_region_at_region_crossings(_Bosl2Base):
    def __init__(self, region1=None, region2=None, closed1=None, closed2=None, eps=None, **kwargs):
       super().__init__("split_region_at_region_crossings", {"region1" : region1, "region2" : region2, "closed1" : closed1, "closed2" : closed2, "eps" : eps, **kwargs})

class region_parts(_Bosl2Base):
    def __init__(self, region=None, **kwargs):
       super().__init__("region_parts", {"region" : region, **kwargs})

class _offset_chamfer(_Bosl2Base):
    def __init__(self, center=None, points=None, delta=None, **kwargs):
       super().__init__("_offset_chamfer", {"center" : center, "points" : points, "delta" : delta, **kwargs})

class _shift_segment(_Bosl2Base):
    def __init__(self, segment=None, d=None, **kwargs):
       super().__init__("_shift_segment", {"segment" : segment, "d" : d, **kwargs})

class _segment_extension(_Bosl2Base):
    def __init__(self, s1=None, s2=None, **kwargs):
       super().__init__("_segment_extension", {"s1" : s1, "s2" : s2, **kwargs})

class _makefaces(_Bosl2Base):
    def __init__(self, direction=None, startind=None, good=None, pointcount=None, closed=None, **kwargs):
       super().__init__("_makefaces", {"direction" : direction, "startind" : startind, "good" : good, "pointcount" : pointcount, "closed" : closed, **kwargs})

class _makefaces_recurse(_Bosl2Base):
    def __init__(self, startind1=None, startind2=None, numfirst=None, numsecond=None, lenlist=None, closed=None, firstind=None, secondind=None, faces=None, **kwargs):
       super().__init__("_makefaces_recurse", {"startind1" : startind1, "startind2" : startind2, "numfirst" : numfirst, "numsecond" : numsecond, "lenlist" : lenlist, "closed" : closed, "firstind" : firstind, "secondind" : secondind, "faces" : faces, **kwargs})

class _good_segments(_Bosl2Base):
    def __init__(self, path=None, d=None, shiftsegs=None, closed=None, quality=None, **kwargs):
       super().__init__("_good_segments", {"path" : path, "d" : d, "shiftsegs" : shiftsegs, "closed" : closed, "quality" : quality, **kwargs})

class _segment_good(_Bosl2Base):
    def __init__(self, path=None, pathseg_unit=None, pathseg_len=None, d=None, seg=None, alpha=None, index=None, **kwargs):
       super().__init__("_segment_good", {"path" : path, "pathseg_unit" : pathseg_unit, "pathseg_len" : pathseg_len, "d" : d, "seg" : seg, "alpha" : alpha, "index" : index, **kwargs})

class _point_dist(_Bosl2Base):
    def __init__(self, path=None, pathseg_unit=None, pathseg_len=None, pt=None, **kwargs):
       super().__init__("_point_dist", {"path" : path, "pathseg_unit" : pathseg_unit, "pathseg_len" : pathseg_len, "pt" : pt, **kwargs})

class offset(_Bosl2Base):
    def __init__(self, path=None, r=None, delta=None, chamfer=None, closed=None, check_valid=None, quality=None, error=None, return_faces=None, firstface_index=None, flip_faces=None, same_length=None, **kwargs):
       super().__init__("offset", {"path" : path, "r" : r, "delta" : delta, "chamfer" : chamfer, "closed" : closed, "check_valid" : check_valid, "quality" : quality, "error" : error, "return_faces" : return_faces, "firstface_index" : firstface_index, "flip_faces" : flip_faces, "same_length" : same_length, **kwargs})

class _filter_region_parts(_Bosl2Base):
    def __init__(self, region1=None, region2=None, keep=None, eps=None, **kwargs):
       super().__init__("_filter_region_parts", {"region1" : region1, "region2" : region2, "keep" : keep, "eps" : eps, **kwargs})

class _list_three(_Bosl2Base):
    def __init__(self, a=None, b=None, c=None, **kwargs):
       super().__init__("_list_three", {"a" : a, "b" : b, "c" : c, **kwargs})

class union(_Bosl2Base):
    def __init__(self, regions=None, b=None, c=None, eps=None, **kwargs):
       super().__init__("union", {"regions" : regions, "b" : b, "c" : c, "eps" : eps, **kwargs})

class difference(_Bosl2Base):
    def __init__(self, regions=None, b=None, c=None, eps=None, **kwargs):
       super().__init__("difference", {"regions" : regions, "b" : b, "c" : c, "eps" : eps, **kwargs})

class intersection(_Bosl2Base):
    def __init__(self, regions=None, b=None, c=None, eps=None, **kwargs):
       super().__init__("intersection", {"regions" : regions, "b" : b, "c" : c, "eps" : eps, **kwargs})

class exclusive_or(_Bosl2Base):
    def __init__(self, regions=None, b=None, c=None, eps=None, **kwargs):
       super().__init__("exclusive_or", {"regions" : regions, "b" : b, "c" : c, "eps" : eps, **kwargs})

class hull_region(_Bosl2Base):
    def __init__(self, region=None, **kwargs):
       super().__init__("hull_region", {"region" : region, **kwargs})

class fill(_Bosl2Base):
    def __init__(self, region=None, **kwargs):
       super().__init__("fill", {"region" : region, **kwargs})

class region(_Bosl2Base):
    def __init__(self, r=None, anchor=None, spin=None, cp=None, atype=None, **kwargs):
       super().__init__("region", {"r" : r, "anchor" : anchor, "spin" : spin, "cp" : cp, "atype" : atype, **kwargs})

class debug_region(_Bosl2Base):
    def __init__(self, region=None, vertices=None, edges=None, convexity=None, size=None, **kwargs):
       super().__init__("debug_region", {"region" : region, "vertices" : vertices, "edges" : edges, "convexity" : convexity, "size" : size, **kwargs})

class exclusive_or(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("exclusive_or", {**kwargs})

class hull_region(_Bosl2Base):
    def __init__(self, region=None, **kwargs):
       super().__init__("hull_region", {"region" : region, **kwargs})

