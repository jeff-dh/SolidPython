from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/utility.scad'}", False)

class typeof(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("typeof", {"x" : x, **kwargs})

class is_type(_Bosl2Base):
    def __init__(self, x=None, types=None, **kwargs):
       super().__init__("is_type", {"x" : x, "types" : types, **kwargs})

class is_def(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_def", {"x" : x, **kwargs})

class is_str(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_str", {"x" : x, **kwargs})

class is_int(_Bosl2Base):
    def __init__(self, n=None, **kwargs):
       super().__init__("is_int", {"n" : n, **kwargs})

class is_integer(_Bosl2Base):
    def __init__(self, n=None, **kwargs):
       super().__init__("is_integer", {"n" : n, **kwargs})

class all_integer(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("all_integer", {"x" : x, **kwargs})

class is_nan(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_nan", {"x" : x, **kwargs})

class is_finite(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_finite", {"x" : x, **kwargs})

class is_range(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_range", {"x" : x, **kwargs})

class valid_range(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("valid_range", {"x" : x, **kwargs})

class is_func(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_func", {"x" : x, **kwargs})

class is_consistent(_Bosl2Base):
    def __init__(self, list=None, pattern=None, **kwargs):
       super().__init__("is_consistent", {"list" : list, "pattern" : pattern, **kwargs})

class _list_pattern(_Bosl2Base):
    def __init__(self, list=None, **kwargs):
       super().__init__("_list_pattern", {"list" : list, **kwargs})

class same_shape(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("same_shape", {"a" : a, "b" : b, **kwargs})

class is_bool_list(_Bosl2Base):
    def __init__(self, list=None, length=None, **kwargs):
       super().__init__("is_bool_list", {"list" : list, "length" : length, **kwargs})

class any(_Bosl2Base):
    def __init__(self, l=None, func=None, **kwargs):
       super().__init__("any", {"l" : l, "func" : func, **kwargs})

class _any_func(_Bosl2Base):
    def __init__(self, l=None, func=None, i=None, out=None, **kwargs):
       super().__init__("_any_func", {"l" : l, "func" : func, "i" : i, "out" : out, **kwargs})

class _any_bool(_Bosl2Base):
    def __init__(self, l=None, i=None, out=None, **kwargs):
       super().__init__("_any_bool", {"l" : l, "i" : i, "out" : out, **kwargs})

class all(_Bosl2Base):
    def __init__(self, l=None, func=None, **kwargs):
       super().__init__("all", {"l" : l, "func" : func, **kwargs})

class _all_func(_Bosl2Base):
    def __init__(self, l=None, func=None, i=None, out=None, **kwargs):
       super().__init__("_all_func", {"l" : l, "func" : func, "i" : i, "out" : out, **kwargs})

class _all_bool(_Bosl2Base):
    def __init__(self, l=None, i=None, out=None, **kwargs):
       super().__init__("_all_bool", {"l" : l, "i" : i, "out" : out, **kwargs})

class num_true(_Bosl2Base):
    def __init__(self, l=None, func=None, **kwargs):
       super().__init__("num_true", {"l" : l, "func" : func, **kwargs})

class default(_Bosl2Base):
    def __init__(self, v=None, dflt=None, **kwargs):
       super().__init__("default", {"v" : v, "dflt" : dflt, **kwargs})

class first_defined(_Bosl2Base):
    def __init__(self, v=None, recursive=None, _i=None, **kwargs):
       super().__init__("first_defined", {"v" : v, "recursive" : recursive, "_i" : _i, **kwargs})

class one_defined(_Bosl2Base):
    def __init__(self, vals=None, names=None, dflt=None, **kwargs):
       super().__init__("one_defined", {"vals" : vals, "names" : names, "dflt" : dflt, **kwargs})

class num_defined(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("num_defined", {"v" : v, **kwargs})

class any_defined(_Bosl2Base):
    def __init__(self, v=None, recursive=None, **kwargs):
       super().__init__("any_defined", {"v" : v, "recursive" : recursive, **kwargs})

class all_defined(_Bosl2Base):
    def __init__(self, v=None, recursive=None, **kwargs):
       super().__init__("all_defined", {"v" : v, "recursive" : recursive, **kwargs})

class u_add(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("u_add", {"a" : a, "b" : b, **kwargs})

class u_sub(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("u_sub", {"a" : a, "b" : b, **kwargs})

class u_mul(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("u_mul", {"a" : a, "b" : b, **kwargs})

class u_div(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("u_div", {"a" : a, "b" : b, **kwargs})

class get_anchor(_Bosl2Base):
    def __init__(self, anchor=None, center=None, uncentered=None, dflt=None, **kwargs):
       super().__init__("get_anchor", {"anchor" : anchor, "center" : center, "uncentered" : uncentered, "dflt" : dflt, **kwargs})

class get_radius(_Bosl2Base):
    def __init__(self, r1=None, r2=None, r=None, d1=None, d2=None, d=None, dflt=None, **kwargs):
       super().__init__("get_radius", {"r1" : r1, "r2" : r2, "r" : r, "d1" : d1, "d2" : d2, "d" : d, "dflt" : dflt, **kwargs})

class scalar_vec3(_Bosl2Base):
    def __init__(self, v=None, dflt=None, **kwargs):
       super().__init__("scalar_vec3", {"v" : v, "dflt" : dflt, **kwargs})

class segs(_Bosl2Base):
    def __init__(self, r=None, **kwargs):
       super().__init__("segs", {"r" : r, **kwargs})

class no_function(_Bosl2Base):
    def __init__(self, name=None, **kwargs):
       super().__init__("no_function", {"name" : name, **kwargs})

class _valstr(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("_valstr", {"x" : x, **kwargs})

class looping(_Bosl2Base):
    def __init__(self, state=None, **kwargs):
       super().__init__("looping", {"state" : state, **kwargs})

class loop_while(_Bosl2Base):
    def __init__(self, state=None, _continue=None, **kwargs):
       super().__init__("loop_while", {"state" : state, "_continue" : _continue, **kwargs})

class loop_done(_Bosl2Base):
    def __init__(self, state=None, **kwargs):
       super().__init__("loop_done", {"state" : state, **kwargs})

class no_children(_Bosl2Base):
    def __init__(self, count=None, **kwargs):
       super().__init__("no_children", {"count" : count, **kwargs})

class req_children(_Bosl2Base):
    def __init__(self, count=None, **kwargs):
       super().__init__("req_children", {"count" : count, **kwargs})

class no_module(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("no_module", {**kwargs})

class deprecate(_Bosl2Base):
    def __init__(self, new_name=None, **kwargs):
       super().__init__("deprecate", {"new_name" : new_name, **kwargs})

class echo_viewport(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("echo_viewport", {**kwargs})

class assert_approx(_Bosl2Base):
    def __init__(self, got=None, expected=None, info=None, **kwargs):
       super().__init__("assert_approx", {"got" : got, "expected" : expected, "info" : info, **kwargs})

class assert_equal(_Bosl2Base):
    def __init__(self, got=None, expected=None, info=None, **kwargs):
       super().__init__("assert_equal", {"got" : got, "expected" : expected, "info" : info, **kwargs})

class shape_compare(_Bosl2Base):
    def __init__(self, eps=None, **kwargs):
       super().__init__("shape_compare", {"eps" : eps, **kwargs})

