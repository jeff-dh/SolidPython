from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/beziers.scad'}", False)

_bezier_matrix_table = _OpenSCADConstant('_bezier_matrix_table')
class bezier_points(_Bosl2Base):
    def __init__(self, curve=None, u=None, **kwargs):
       super().__init__("bezier_points", {"curve" : curve, "u" : u, **kwargs})

class _signed_pascals_triangle(_Bosl2Base):
    def __init__(self, N=None, tri=None, **kwargs):
       super().__init__("_signed_pascals_triangle", {"N" : N, "tri" : tri, **kwargs})

class _compute_bezier_matrix(_Bosl2Base):
    def __init__(self, N=None, **kwargs):
       super().__init__("_compute_bezier_matrix", {"N" : N, **kwargs})

class _bezier_matrix(_Bosl2Base):
    def __init__(self, N=None, **kwargs):
       super().__init__("_bezier_matrix", {"N" : N, **kwargs})

class bezier_curve(_Bosl2Base):
    def __init__(self, bezier=None, splinesteps=None, endpoint=None, **kwargs):
       super().__init__("bezier_curve", {"bezier" : bezier, "splinesteps" : splinesteps, "endpoint" : endpoint, **kwargs})

class bezier_derivative(_Bosl2Base):
    def __init__(self, bezier=None, u=None, order=None, **kwargs):
       super().__init__("bezier_derivative", {"bezier" : bezier, "u" : u, "order" : order, **kwargs})

class bezier_tangent(_Bosl2Base):
    def __init__(self, bezier=None, u=None, **kwargs):
       super().__init__("bezier_tangent", {"bezier" : bezier, "u" : u, **kwargs})

class bezier_curvature(_Bosl2Base):
    def __init__(self, bezier=None, u=None, **kwargs):
       super().__init__("bezier_curvature", {"bezier" : bezier, "u" : u, **kwargs})

class bezier_closest_point(_Bosl2Base):
    def __init__(self, bezier=None, pt=None, max_err=None, u=None, end_u=None, **kwargs):
       super().__init__("bezier_closest_point", {"bezier" : bezier, "pt" : pt, "max_err" : max_err, "u" : u, "end_u" : end_u, **kwargs})

class bezier_length(_Bosl2Base):
    def __init__(self, bezier=None, start_u=None, end_u=None, max_deflect=None, **kwargs):
       super().__init__("bezier_length", {"bezier" : bezier, "start_u" : start_u, "end_u" : end_u, "max_deflect" : max_deflect, **kwargs})

class bezier_line_intersection(_Bosl2Base):
    def __init__(self, bezier=None, line=None, **kwargs):
       super().__init__("bezier_line_intersection", {"bezier" : bezier, "line" : line, **kwargs})

class bezpath_points(_Bosl2Base):
    def __init__(self, bezpath=None, curveind=None, u=None, N=None, **kwargs):
       super().__init__("bezpath_points", {"bezpath" : bezpath, "curveind" : curveind, "u" : u, "N" : N, **kwargs})

class bezpath_curve(_Bosl2Base):
    def __init__(self, bezpath=None, splinesteps=None, N=None, endpoint=None, **kwargs):
       super().__init__("bezpath_curve", {"bezpath" : bezpath, "splinesteps" : splinesteps, "N" : N, "endpoint" : endpoint, **kwargs})

class bezpath_closest_point(_Bosl2Base):
    def __init__(self, bezpath=None, pt=None, N=None, max_err=None, seg=None, min_seg=None, min_u=None, min_dist=None, **kwargs):
       super().__init__("bezpath_closest_point", {"bezpath" : bezpath, "pt" : pt, "N" : N, "max_err" : max_err, "seg" : seg, "min_seg" : min_seg, "min_u" : min_u, "min_dist" : min_dist, **kwargs})

class bezpath_length(_Bosl2Base):
    def __init__(self, bezpath=None, N=None, max_deflect=None, **kwargs):
       super().__init__("bezpath_length", {"bezpath" : bezpath, "N" : N, "max_deflect" : max_deflect, **kwargs})

class path_to_bezpath(_Bosl2Base):
    def __init__(self, path=None, closed=None, tangents=None, uniform=None, size=None, relsize=None, **kwargs):
       super().__init__("path_to_bezpath", {"path" : path, "closed" : closed, "tangents" : tangents, "uniform" : uniform, "size" : size, "relsize" : relsize, **kwargs})

class path_to_bezcornerpath(_Bosl2Base):
    def __init__(self, path=None, closed=None, size=None, relsize=None, **kwargs):
       super().__init__("path_to_bezcornerpath", {"path" : path, "closed" : closed, "size" : size, "relsize" : relsize, **kwargs})

class _bez_path_corner(_Bosl2Base):
    def __init__(self, p=None, curvesize=None, relative=None, mincurvesize=None, **kwargs):
       super().__init__("_bez_path_corner", {"p" : p, "curvesize" : curvesize, "relative" : relative, "mincurvesize" : mincurvesize, **kwargs})

class bezpath_close_to_axis(_Bosl2Base):
    def __init__(self, bezpath=None, axis=None, N=None, **kwargs):
       super().__init__("bezpath_close_to_axis", {"bezpath" : bezpath, "axis" : axis, "N" : N, **kwargs})

class bezpath_offset(_Bosl2Base):
    def __init__(self, offset=None, bezier=None, N=None, **kwargs):
       super().__init__("bezpath_offset", {"offset" : offset, "bezier" : bezier, "N" : N, **kwargs})

class bez_begin(_Bosl2Base):
    def __init__(self, pt=None, a=None, r=None, p=None, **kwargs):
       super().__init__("bez_begin", {"pt" : pt, "a" : a, "r" : r, "p" : p, **kwargs})

class bez_tang(_Bosl2Base):
    def __init__(self, pt=None, a=None, r1=None, r2=None, p=None, **kwargs):
       super().__init__("bez_tang", {"pt" : pt, "a" : a, "r1" : r1, "r2" : r2, "p" : p, **kwargs})

class bez_joint(_Bosl2Base):
    def __init__(self, pt=None, a1=None, a2=None, r1=None, r2=None, p1=None, p2=None, **kwargs):
       super().__init__("bez_joint", {"pt" : pt, "a1" : a1, "a2" : a2, "r1" : r1, "r2" : r2, "p1" : p1, "p2" : p2, **kwargs})

class bez_end(_Bosl2Base):
    def __init__(self, pt=None, a=None, r=None, p=None, **kwargs):
       super().__init__("bez_end", {"pt" : pt, "a" : a, "r" : r, "p" : p, **kwargs})

class is_bezier_patch(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_bezier_patch", {"x" : x, **kwargs})

class bezier_patch_flat(_Bosl2Base):
    def __init__(self, size=None, N=None, spin=None, orient=None, trans=None, **kwargs):
       super().__init__("bezier_patch_flat", {"size" : size, "N" : N, "spin" : spin, "orient" : orient, "trans" : trans, **kwargs})

class bezier_patch_reverse(_Bosl2Base):
    def __init__(self, patch=None, **kwargs):
       super().__init__("bezier_patch_reverse", {"patch" : patch, **kwargs})

class bezier_patch_points(_Bosl2Base):
    def __init__(self, patch=None, u=None, v=None, **kwargs):
       super().__init__("bezier_patch_points", {"patch" : patch, "u" : u, "v" : v, **kwargs})

class _bezier_rectangle(_Bosl2Base):
    def __init__(self, patch=None, splinesteps=None, style=None, **kwargs):
       super().__init__("_bezier_rectangle", {"patch" : patch, "splinesteps" : splinesteps, "style" : style, **kwargs})

class bezier_vnf(_Bosl2Base):
    def __init__(self, patches=None, splinesteps=None, style=None, **kwargs):
       super().__init__("bezier_vnf", {"patches" : patches, "splinesteps" : splinesteps, "style" : style, **kwargs})

class bezier_vnf_degenerate_patch(_Bosl2Base):
    def __init__(self, patch=None, splinesteps=None, reverse=None, return_edges=None, **kwargs):
       super().__init__("bezier_vnf_degenerate_patch", {"patch" : patch, "splinesteps" : splinesteps, "reverse" : reverse, "return_edges" : return_edges, **kwargs})

class bezier_patch_normals(_Bosl2Base):
    def __init__(self, patch=None, u=None, v=None, **kwargs):
       super().__init__("bezier_patch_normals", {"patch" : patch, "u" : u, "v" : v, **kwargs})

class bezier_sheet(_Bosl2Base):
    def __init__(self, patch=None, delta=None, splinesteps=None, style=None, thickness=None, **kwargs):
       super().__init__("bezier_sheet", {"patch" : patch, "delta" : delta, "splinesteps" : splinesteps, "style" : style, "thickness" : thickness, **kwargs})

class debug_bezier(_Bosl2Base):
    def __init__(self, bezpath=None, width=None, N=None, **kwargs):
       super().__init__("debug_bezier", {"bezpath" : bezpath, "width" : width, "N" : N, **kwargs})

class debug_bezier_patches(_Bosl2Base):
    def __init__(self, patches=None, size=None, splinesteps=None, showcps=None, showdots=None, showpatch=None, convexity=None, style=None, **kwargs):
       super().__init__("debug_bezier_patches", {"patches" : patches, "size" : size, "splinesteps" : splinesteps, "showcps" : showcps, "showdots" : showdots, "showpatch" : showpatch, "convexity" : convexity, "style" : style, **kwargs})

