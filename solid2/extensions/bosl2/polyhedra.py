from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/polyhedra.scad'}", False)

_tribonacci = _OpenSCADConstant('_tribonacci')
_polyhedra_ = _OpenSCADConstant('_polyhedra_')
_stellated_polyhedra_ = _OpenSCADConstant('_stellated_polyhedra_')
class _unique_groups(_Bosl2Base):
    def __init__(self, m=None, **kwargs):
       super().__init__("_unique_groups", {"m" : m, **kwargs})

class _even_perms(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("_even_perms", {"v" : v, **kwargs})

class _all_perms(_Bosl2Base):
    def __init__(self, v=None, **kwargs):
       super().__init__("_all_perms", {"v" : v, **kwargs})

class _point_ref(_Bosl2Base):
    def __init__(self, points=None, sign=None, **kwargs):
       super().__init__("_point_ref", {"points" : points, "sign" : sign, **kwargs})

class regular_polyhedron_info(_Bosl2Base):
    def __init__(self, info=None, name=None, index=None, type=None, faces=None, facetype=None, hasfaces=None, side=None, ir=None, mr=None, _or=None, r=None, d=None, anchor=None, facedown=None, stellate=None, longside=None, h=None, height=None, **kwargs):
       super().__init__("regular_polyhedron_info", {"info" : info, "name" : name, "index" : index, "type" : type, "faces" : faces, "facetype" : facetype, "hasfaces" : hasfaces, "side" : side, "ir" : ir, "mr" : mr, "_or" : _or, "r" : r, "d" : d, "anchor" : anchor, "facedown" : facedown, "stellate" : stellate, "longside" : longside, "h" : h, "height" : height, **kwargs})

class _stellate_faces(_Bosl2Base):
    def __init__(self, scalefactor=None, stellate=None, vertices=None, faces_normals=None, **kwargs):
       super().__init__("_stellate_faces", {"scalefactor" : scalefactor, "stellate" : stellate, "vertices" : vertices, "faces_normals" : faces_normals, **kwargs})

class _trapezohedron(_Bosl2Base):
    def __init__(self, faces=None, r=None, side=None, longside=None, h=None, height=None, d=None, **kwargs):
       super().__init__("_trapezohedron", {"faces" : faces, "r" : r, "side" : side, "longside" : longside, "h" : h, "height" : height, "d" : d, **kwargs})

class _facenormal(_Bosl2Base):
    def __init__(self, pts=None, face=None, **kwargs):
       super().__init__("_facenormal", {"pts" : pts, "face" : face, **kwargs})

class _full_faces(_Bosl2Base):
    def __init__(self, pts=None, faces=None, **kwargs):
       super().__init__("_full_faces", {"pts" : pts, "faces" : faces, **kwargs})

class regular_polyhedron(_Bosl2Base):
    def __init__(self, name=None, index=None, type=None, faces=None, facetype=None, hasfaces=None, side=None, ir=None, mr=None, _or=None, r=None, d=None, anchor=None, rounding=None, repeat=None, facedown=None, draw=None, rotate_children=None, stellate=None, longside=None, h=None, height=None, **kwargs):
       super().__init__("regular_polyhedron", {"name" : name, "index" : index, "type" : type, "faces" : faces, "facetype" : facetype, "hasfaces" : hasfaces, "side" : side, "ir" : ir, "mr" : mr, "_or" : _or, "r" : r, "d" : d, "anchor" : anchor, "rounding" : rounding, "repeat" : repeat, "facedown" : facedown, "draw" : draw, "rotate_children" : rotate_children, "stellate" : stellate, "longside" : longside, "h" : h, "height" : height, **kwargs})

