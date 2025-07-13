from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/math.scad'}", False)

PHI = _OpenSCADConstant('PHI')
EPSILON = _OpenSCADConstant('EPSILON')
INF = _OpenSCADConstant('INF')
NAN = _OpenSCADConstant('NAN')
class count(_Bosl2Base):
    def __init__(self, n=None, s=None, step=None, reverse=None, **kwargs):
       super().__init__("count", {"n" : n, "s" : s, "step" : step, "reverse" : reverse, **kwargs})

class lerp(_Bosl2Base):
    def __init__(self, a=None, b=None, u=None, **kwargs):
       super().__init__("lerp", {"a" : a, "b" : b, "u" : u, **kwargs})

class lerpn(_Bosl2Base):
    def __init__(self, a=None, b=None, n=None, endpoint=None, **kwargs):
       super().__init__("lerpn", {"a" : a, "b" : b, "n" : n, "endpoint" : endpoint, **kwargs})

class bilerp(_Bosl2Base):
    def __init__(self, points=None, x=None, y=None, **kwargs):
       super().__init__("bilerp", {"points" : points, "x" : x, "y" : y, **kwargs})

class sqr(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("sqr", {"x" : x, **kwargs})

class log2(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("log2", {"x" : x, **kwargs})

class hypot(_Bosl2Base):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("hypot", {"x" : x, "y" : y, "z" : z, **kwargs})

class factorial(_Bosl2Base):
    def __init__(self, n=None, d=None, **kwargs):
       super().__init__("factorial", {"n" : n, "d" : d, **kwargs})

class binomial(_Bosl2Base):
    def __init__(self, n=None, **kwargs):
       super().__init__("binomial", {"n" : n, **kwargs})

class binomial_coefficient(_Bosl2Base):
    def __init__(self, n=None, k=None, **kwargs):
       super().__init__("binomial_coefficient", {"n" : n, "k" : k, **kwargs})

class gcd(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("gcd", {"a" : a, "b" : b, **kwargs})

class _lcm(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("_lcm", {"a" : a, "b" : b, **kwargs})

class _lcmlist(_Bosl2Base):
    def __init__(self, a=None, **kwargs):
       super().__init__("_lcmlist", {"a" : a, **kwargs})

class lcm(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("lcm", {"a" : a, "b" : b, **kwargs})

class rational_approx(_Bosl2Base):
    def __init__(self, x=None, maxq=None, cfrac=None, p=None, q=None, **kwargs):
       super().__init__("rational_approx", {"x" : x, "maxq" : maxq, "cfrac" : cfrac, "p" : p, "q" : q, **kwargs})

class _cfrac_to_pq(_Bosl2Base):
    def __init__(self, cfrac=None, p=None, q=None, ind=None, **kwargs):
       super().__init__("_cfrac_to_pq", {"cfrac" : cfrac, "p" : p, "q" : q, "ind" : ind, **kwargs})

class sinh(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("sinh", {"x" : x, **kwargs})

class cosh(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("cosh", {"x" : x, **kwargs})

class tanh(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("tanh", {"x" : x, **kwargs})

class asinh(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("asinh", {"x" : x, **kwargs})

class acosh(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("acosh", {"x" : x, **kwargs})

class atanh(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("atanh", {"x" : x, **kwargs})

class quant(_Bosl2Base):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quant", {"x" : x, "y" : y, **kwargs})

class _roundall(_Bosl2Base):
    def __init__(self, data=None, **kwargs):
       super().__init__("_roundall", {"data" : data, **kwargs})

class quantdn(_Bosl2Base):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quantdn", {"x" : x, "y" : y, **kwargs})

class _floorall(_Bosl2Base):
    def __init__(self, data=None, **kwargs):
       super().__init__("_floorall", {"data" : data, **kwargs})

class quantup(_Bosl2Base):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quantup", {"x" : x, "y" : y, **kwargs})

class _ceilall(_Bosl2Base):
    def __init__(self, data=None, **kwargs):
       super().__init__("_ceilall", {"data" : data, **kwargs})

class constrain(_Bosl2Base):
    def __init__(self, v=None, minval=None, maxval=None, **kwargs):
       super().__init__("constrain", {"v" : v, "minval" : minval, "maxval" : maxval, **kwargs})

class posmod(_Bosl2Base):
    def __init__(self, x=None, m=None, **kwargs):
       super().__init__("posmod", {"x" : x, "m" : m, **kwargs})

class modang(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("modang", {"x" : x, **kwargs})

class mean_angle(_Bosl2Base):
    def __init__(self, angle1=None, angle2=None, **kwargs):
       super().__init__("mean_angle", {"angle1" : angle1, "angle2" : angle2, **kwargs})

class fit_to_range(_Bosl2Base):
    def __init__(self, M=None, minval=None, maxval=None, **kwargs):
       super().__init__("fit_to_range", {"M" : M, "minval" : minval, "maxval" : maxval, **kwargs})

class sum(_Bosl2Base):
    def __init__(self, v=None, dflt=None, **kwargs):
       super().__init__("sum", {"v" : v, "dflt" : dflt, **kwargs})

class _sum(_Bosl2Base):
    def __init__(self, v=None, _total=None, _i=None, **kwargs):
       super().__init__("_sum", {"v" : v, "_total" : _total, "_i" : _i, **kwargs})

class mean(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("mean", {"v" : v, **kwargs})

class median(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("median", {"v" : v, **kwargs})

class deltas(_Bosl2Base):
    def __init__(self, v=None, wrap=None, **kwargs):
       super().__init__("deltas", {"v" : v, "wrap" : wrap, **kwargs})

class cumsum(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("cumsum", {"v" : v, **kwargs})

class product(_Bosl2Base):
    def __init__(self, list=None, right=None, **kwargs):
       super().__init__("product", {"list" : list, "right" : right, **kwargs})

class cumprod(_Bosl2Base):
    def __init__(self, list=None, right=None, **kwargs):
       super().__init__("cumprod", {"list" : list, "right" : right, **kwargs})

class convolve(_Bosl2Base):
    def __init__(self, p=None, q=None, **kwargs):
       super().__init__("convolve", {"p" : p, "q" : q, **kwargs})

class sum_of_sines(_Bosl2Base):
    def __init__(self, a=None, sines=None, **kwargs):
       super().__init__("sum_of_sines", {"a" : a, "sines" : sines, **kwargs})

class rand_int(_Bosl2Base):
    def __init__(self, minval=None, maxval=None, n=None, seed=None, **kwargs):
       super().__init__("rand_int", {"minval" : minval, "maxval" : maxval, "n" : n, "seed" : seed, **kwargs})

class random_points(_Bosl2Base):
    def __init__(self, n=None, dim=None, scale=None, seed=None, **kwargs):
       super().__init__("random_points", {"n" : n, "dim" : dim, "scale" : scale, "seed" : seed, **kwargs})

class gaussian_rands(_Bosl2Base):
    def __init__(self, n=None, mean=None, cov=None, seed=None, **kwargs):
       super().__init__("gaussian_rands", {"n" : n, "mean" : mean, "cov" : cov, "seed" : seed, **kwargs})

class exponential_rands(_Bosl2Base):
    def __init__(self, n=None, _lambda=None, seed=None, **kwargs):
       super().__init__("exponential_rands", {"n" : n, "_lambda" : _lambda, "seed" : seed, **kwargs})

class spherical_random_points(_Bosl2Base):
    def __init__(self, n=None, radius=None, seed=None, **kwargs):
       super().__init__("spherical_random_points", {"n" : n, "radius" : radius, "seed" : seed, **kwargs})

class random_polygon(_Bosl2Base):
    def __init__(self, n=None, size=None, seed=None, **kwargs):
       super().__init__("random_polygon", {"n" : n, "size" : size, "seed" : seed, **kwargs})

class deriv(_Bosl2Base):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("deriv", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class _dnu_calc(_Bosl2Base):
    def __init__(self, f1=None, fc=None, f2=None, h1=None, h2=None, **kwargs):
       super().__init__("_dnu_calc", {"f1" : f1, "fc" : fc, "f2" : f2, "h1" : h1, "h2" : h2, **kwargs})

class _deriv_nonuniform(_Bosl2Base):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("_deriv_nonuniform", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class deriv2(_Bosl2Base):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("deriv2", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class deriv3(_Bosl2Base):
    def __init__(self, data=None, h=None, closed=None, **kwargs):
       super().__init__("deriv3", {"data" : data, "h" : h, "closed" : closed, **kwargs})

class complex(_Bosl2Base):
    def __init__(self, list=None, **kwargs):
       super().__init__("complex", {"list" : list, **kwargs})

class c_mul(_Bosl2Base):
    def __init__(self, z1=None, z2=None, **kwargs):
       super().__init__("c_mul", {"z1" : z1, "z2" : z2, **kwargs})

class _split_complex(_Bosl2Base):
    def __init__(self, data=None, **kwargs):
       super().__init__("_split_complex", {"data" : data, **kwargs})

class _combine_complex(_Bosl2Base):
    def __init__(self, data=None, **kwargs):
       super().__init__("_combine_complex", {"data" : data, **kwargs})

class _c_mul(_Bosl2Base):
    def __init__(self, z1=None, z2=None, **kwargs):
       super().__init__("_c_mul", {"z1" : z1, "z2" : z2, **kwargs})

class c_div(_Bosl2Base):
    def __init__(self, z1=None, z2=None, **kwargs):
       super().__init__("c_div", {"z1" : z1, "z2" : z2, **kwargs})

class c_conj(_Bosl2Base):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_conj", {"z" : z, **kwargs})

class c_real(_Bosl2Base):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_real", {"z" : z, **kwargs})

class c_imag(_Bosl2Base):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_imag", {"z" : z, **kwargs})

class c_ident(_Bosl2Base):
    def __init__(self, n=None, **kwargs):
       super().__init__("c_ident", {"n" : n, **kwargs})

class c_norm(_Bosl2Base):
    def __init__(self, z=None, **kwargs):
       super().__init__("c_norm", {"z" : z, **kwargs})

class quadratic_roots(_Bosl2Base):
    def __init__(self, a=None, b=None, c=None, real=None, **kwargs):
       super().__init__("quadratic_roots", {"a" : a, "b" : b, "c" : c, "real" : real, **kwargs})

class polynomial(_Bosl2Base):
    def __init__(self, p=None, z=None, k=None, total=None, **kwargs):
       super().__init__("polynomial", {"p" : p, "z" : z, "k" : k, "total" : total, **kwargs})

class poly_mult(_Bosl2Base):
    def __init__(self, p=None, q=None, **kwargs):
       super().__init__("poly_mult", {"p" : p, "q" : q, **kwargs})

class poly_div(_Bosl2Base):
    def __init__(self, n=None, d=None, **kwargs):
       super().__init__("poly_div", {"n" : n, "d" : d, **kwargs})

class _poly_div(_Bosl2Base):
    def __init__(self, n=None, d=None, q=None, **kwargs):
       super().__init__("_poly_div", {"n" : n, "d" : d, "q" : q, **kwargs})

class _poly_trim(_Bosl2Base):
    def __init__(self, p=None, eps=None, **kwargs):
       super().__init__("_poly_trim", {"p" : p, "eps" : eps, **kwargs})

class poly_add(_Bosl2Base):
    def __init__(self, p=None, q=None, **kwargs):
       super().__init__("poly_add", {"p" : p, "q" : q, **kwargs})

class poly_roots(_Bosl2Base):
    def __init__(self, p=None, tol=None, error_bound=None, **kwargs):
       super().__init__("poly_roots", {"p" : p, "tol" : tol, "error_bound" : error_bound, **kwargs})

class _poly_roots(_Bosl2Base):
    def __init__(self, p=None, pderiv=None, s=None, z=None, tol=None, i=None, **kwargs):
       super().__init__("_poly_roots", {"p" : p, "pderiv" : pderiv, "s" : s, "z" : z, "tol" : tol, "i" : i, **kwargs})

class real_roots(_Bosl2Base):
    def __init__(self, p=None, eps=None, tol=None, **kwargs):
       super().__init__("real_roots", {"p" : p, "eps" : eps, "tol" : tol, **kwargs})

class root_find(_Bosl2Base):
    def __init__(self, f=None, x0=None, x1=None, tol=None, **kwargs):
       super().__init__("root_find", {"f" : f, "x0" : x0, "x1" : x1, "tol" : tol, **kwargs})

class _rfcheck(_Bosl2Base):
    def __init__(self, x=None, y=None, range=None, tol=None, **kwargs):
       super().__init__("_rfcheck", {"x" : x, "y" : y, "range" : range, "tol" : tol, **kwargs})

class _rootfind(_Bosl2Base):
    def __init__(self, f=None, xpts=None, ypts=None, yrange=None, tol=None, i=None, **kwargs):
       super().__init__("_rootfind", {"f" : f, "xpts" : xpts, "ypts" : ypts, "yrange" : yrange, "tol" : tol, "i" : i, **kwargs})

