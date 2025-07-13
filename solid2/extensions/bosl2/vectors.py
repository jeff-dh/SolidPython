from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/vectors.scad'}", False)

class is_vector(_Bosl2Base):
    def __init__(self, v=None, length=None, zero=None, all_nonzero=None, eps=None, **kwargs):
       super().__init__("is_vector", {"v" : v, "length" : length, "zero" : zero, "all_nonzero" : all_nonzero, "eps" : eps, **kwargs})

class add_scalar(_Bosl2Base):
    def __init__(self, v=None, s=None, **kwargs):
       super().__init__("add_scalar", {"v" : v, "s" : s, **kwargs})

class v_mul(_Bosl2Base):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("v_mul", {"v1" : v1, "v2" : v2, **kwargs})

class v_div(_Bosl2Base):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("v_div", {"v1" : v1, "v2" : v2, **kwargs})

class v_abs(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_abs", {"v" : v, **kwargs})

class v_ceil(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_ceil", {"v" : v, **kwargs})

class v_floor(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_floor", {"v" : v, **kwargs})

class v_round(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_round", {"v" : v, **kwargs})

class v_lookup(_Bosl2Base):
    def __init__(self, x=None, v=None, **kwargs):
       super().__init__("v_lookup", {"x" : x, "v" : v, **kwargs})

class unit(_Bosl2Base):
    def __init__(self, v=None, error=None, **kwargs):
       super().__init__("unit", {"v" : v, "error" : error, **kwargs})

class v_theta(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_theta", {"v" : v, **kwargs})

class vector_angle(_Bosl2Base):
    def __init__(self, v1=None, v2=None, v3=None, **kwargs):
       super().__init__("vector_angle", {"v1" : v1, "v2" : v2, "v3" : v3, **kwargs})

class vector_axis(_Bosl2Base):
    def __init__(self, v1=None, v2=None, v3=None, **kwargs):
       super().__init__("vector_axis", {"v1" : v1, "v2" : v2, "v3" : v3, **kwargs})

class vector_bisect(_Bosl2Base):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("vector_bisect", {"v1" : v1, "v2" : v2, **kwargs})

class vector_perp(_Bosl2Base):
    def __init__(self, v=None, w=None, **kwargs):
       super().__init__("vector_perp", {"v" : v, "w" : w, **kwargs})

class closest_point(_Bosl2Base):
    def __init__(self, pt=None, points=None, **kwargs):
       super().__init__("closest_point", {"pt" : pt, "points" : points, **kwargs})

class furthest_point(_Bosl2Base):
    def __init__(self, pt=None, points=None, **kwargs):
       super().__init__("furthest_point", {"pt" : pt, "points" : points, **kwargs})

class vector_search(_Bosl2Base):
    def __init__(self, query=None, r=None, target=None, **kwargs):
       super().__init__("vector_search", {"query" : query, "r" : r, "target" : target, **kwargs})

class _bt_search(_Bosl2Base):
    def __init__(self, query=None, r=None, points=None, tree=None, **kwargs):
       super().__init__("_bt_search", {"query" : query, "r" : r, "points" : points, "tree" : tree, **kwargs})

class vector_search_tree(_Bosl2Base):
    def __init__(self, points=None, leafsize=None, treemin=None, **kwargs):
       super().__init__("vector_search_tree", {"points" : points, "leafsize" : leafsize, "treemin" : treemin, **kwargs})

class _bt_tree(_Bosl2Base):
    def __init__(self, points=None, ind=None, leafsize=None, **kwargs):
       super().__init__("_bt_tree", {"points" : points, "ind" : ind, "leafsize" : leafsize, **kwargs})

class vector_nearest(_Bosl2Base):
    def __init__(self, query=None, k=None, target=None, **kwargs):
       super().__init__("vector_nearest", {"query" : query, "k" : k, "target" : target, **kwargs})

class _bt_nearest(_Bosl2Base):
    def __init__(self, p=None, k=None, points=None, tree=None, answers=None, **kwargs):
       super().__init__("_bt_nearest", {"p" : p, "k" : k, "points" : points, "tree" : tree, "answers" : answers, **kwargs})

class _insert_sorted(_Bosl2Base):
    def __init__(self, list=None, k=None, new=None, **kwargs):
       super().__init__("_insert_sorted", {"list" : list, "k" : k, "new" : new, **kwargs})

class _insert_many(_Bosl2Base):
    def __init__(self, list=None, k=None, newlist=None, i=None, **kwargs):
       super().__init__("_insert_many", {"list" : list, "k" : k, "newlist" : newlist, "i" : i, **kwargs})

class pointlist_bounds(_Bosl2Base):
    def __init__(self, pts=None, **kwargs):
       super().__init__("pointlist_bounds", {"pts" : pts, **kwargs})

class fit_to_box(_Bosl2Base):
    def __init__(self, pts=None, x=None, y=None, z=None, **kwargs):
       super().__init__("fit_to_box", {"pts" : pts, "x" : x, "y" : y, "z" : z, **kwargs})

