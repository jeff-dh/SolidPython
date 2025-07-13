from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/isosurface.scad'}", False)

_MCEdgeVertexIndices = _OpenSCADConstant('_MCEdgeVertexIndices')
_MCTriangleTable = _OpenSCADConstant('_MCTriangleTable')
_MCTriangleTable_reverse = _OpenSCADConstant('_MCTriangleTable_reverse')
_MCFaceVertexIndices = _OpenSCADConstant('_MCFaceVertexIndices')
_MCClipEdgeVertexIndices = _OpenSCADConstant('_MCClipEdgeVertexIndices')
_MCClipTriangleTable = _OpenSCADConstant('_MCClipTriangleTable')
_MTEdgeVertexIndices = _OpenSCADConstant('_MTEdgeVertexIndices')
_MTriSegmentTable = _OpenSCADConstant('_MTriSegmentTable')
_MTriSegmentTable_reverse = _OpenSCADConstant('_MTriSegmentTable_reverse')
_MSquareSegmentTable = _OpenSCADConstant('_MSquareSegmentTable')
_MSquareSegmentTable_reverse = _OpenSCADConstant('_MSquareSegmentTable_reverse')
_metaball_vnf = _OpenSCADConstant('_metaball_vnf')
class _cubeindex(_Bosl2Base):
    def __init__(self, f=None, isoval=None, **kwargs):
       super().__init__("_cubeindex", {"f" : f, "isoval" : isoval, **kwargs})

class _clipfacindex(_Bosl2Base):
    def __init__(self, f=None, isovalmin=None, isovalmax=None, **kwargs):
       super().__init__("_clipfacindex", {"f" : f, "isovalmin" : isovalmin, "isovalmax" : isovalmax, **kwargs})

class _bbox_faces(_Bosl2Base):
    def __init__(self, v0=None, voxsize=None, bbox=None, **kwargs):
       super().__init__("_bbox_faces", {"v0" : v0, "voxsize" : voxsize, "bbox" : bbox, **kwargs})

class _isosurface_cubes(_Bosl2Base):
    def __init__(self, voxsize=None, bbox=None, fieldarray=None, fieldfunc=None, isovalmin=None, isovalmax=None, closed=None, **kwargs):
       super().__init__("_isosurface_cubes", {"voxsize" : voxsize, "bbox" : bbox, "fieldarray" : fieldarray, "fieldfunc" : fieldfunc, "isovalmin" : isovalmin, "isovalmax" : isovalmax, "closed" : closed, **kwargs})

class _isosurface_triangles(_Bosl2Base):
    def __init__(self, cubelist=None, voxsize=None, isovalmin=None, isovalmax=None, tritablemin=None, tritablemax=None, **kwargs):
       super().__init__("_isosurface_triangles", {"cubelist" : cubelist, "voxsize" : voxsize, "isovalmin" : isovalmin, "isovalmax" : isovalmax, "tritablemin" : tritablemin, "tritablemax" : tritablemax, **kwargs})

class _clipfacevertices(_Bosl2Base):
    def __init__(self, vcube=None, fld=None, bbface=None, isovalmin=None, isovalmax=None, **kwargs):
       super().__init__("_clipfacevertices", {"vcube" : vcube, "fld" : fld, "bbface" : bbface, "isovalmin" : isovalmin, "isovalmax" : isovalmax, **kwargs})

class _mctrindex(_Bosl2Base):
    def __init__(self, f=None, isoval=None, **kwargs):
       super().__init__("_mctrindex", {"f" : f, "isoval" : isoval, **kwargs})

class _bbox_sides(_Bosl2Base):
    def __init__(self, pc=None, pixsize=None, bbox=None, **kwargs):
       super().__init__("_bbox_sides", {"pc" : pc, "pixsize" : pixsize, "bbox" : bbox, **kwargs})

class _contour_pixels(_Bosl2Base):
    def __init__(self, pixsize=None, bbox=None, fieldarray=None, fieldfunc=None, pixcenters=None, isovalmin=None, isovalmax=None, closed=None, **kwargs):
       super().__init__("_contour_pixels", {"pixsize" : pixsize, "bbox" : bbox, "fieldarray" : fieldarray, "fieldfunc" : fieldfunc, "pixcenters" : pixcenters, "isovalmin" : isovalmin, "isovalmax" : isovalmax, "closed" : closed, **kwargs})

class _contour_vertices(_Bosl2Base):
    def __init__(self, pxlist=None, pxsize=None, isovalmin=None, isovalmax=None, segtablemin=None, segtablemax=None, **kwargs):
       super().__init__("_contour_vertices", {"pxlist" : pxlist, "pxsize" : pxsize, "isovalmin" : isovalmin, "isovalmax" : isovalmax, "segtablemin" : segtablemin, "segtablemax" : segtablemax, **kwargs})

class mb_cutoff(_Bosl2Base):
    def __init__(self, dist=None, cutoff=None, **kwargs):
       super().__init__("mb_cutoff", {"dist" : dist, "cutoff" : cutoff, **kwargs})

class _mb_sphere_basic(_Bosl2Base):
    def __init__(self, point=None, r=None, neg=None, **kwargs):
       super().__init__("_mb_sphere_basic", {"point" : point, "r" : r, "neg" : neg, **kwargs})

class _mb_sphere_influence(_Bosl2Base):
    def __init__(self, point=None, r=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_sphere_influence", {"point" : point, "r" : r, "ex" : ex, "neg" : neg, **kwargs})

class _mb_sphere_cutoff(_Bosl2Base):
    def __init__(self, point=None, r=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_sphere_cutoff", {"point" : point, "r" : r, "cutoff" : cutoff, "neg" : neg, **kwargs})

class _mb_sphere_full(_Bosl2Base):
    def __init__(self, point=None, r=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_sphere_full", {"point" : point, "r" : r, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_sphere(_Bosl2Base):
    def __init__(self, r=None, cutoff=None, influence=None, negative=None, hide_debug=None, d=None, **kwargs):
       super().__init__("mb_sphere", {"r" : r, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d" : d, **kwargs})

class _mb_cuboid_basic(_Bosl2Base):
    def __init__(self, point=None, inv_size=None, xp=None, neg=None, **kwargs):
       super().__init__("_mb_cuboid_basic", {"point" : point, "inv_size" : inv_size, "xp" : xp, "neg" : neg, **kwargs})

class _mb_cuboid_influence(_Bosl2Base):
    def __init__(self, point=None, inv_size=None, xp=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_cuboid_influence", {"point" : point, "inv_size" : inv_size, "xp" : xp, "ex" : ex, "neg" : neg, **kwargs})

class _mb_cuboid_cutoff(_Bosl2Base):
    def __init__(self, point=None, inv_size=None, xp=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_cuboid_cutoff", {"point" : point, "inv_size" : inv_size, "xp" : xp, "cutoff" : cutoff, "neg" : neg, **kwargs})

class _mb_cuboid_full(_Bosl2Base):
    def __init__(self, point=None, inv_size=None, xp=None, ex=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_cuboid_full", {"point" : point, "inv_size" : inv_size, "xp" : xp, "ex" : ex, "cutoff" : cutoff, "neg" : neg, **kwargs})

class mb_cuboid(_Bosl2Base):
    def __init__(self, size=None, squareness=None, cutoff=None, influence=None, negative=None, hide_debug=None, **kwargs):
       super().__init__("mb_cuboid", {"size" : size, "squareness" : squareness, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, **kwargs})

class _revsurf_basic(_Bosl2Base):
    def __init__(self, point=None, path=None, coef=None, neg=None, maxdist=None, **kwargs):
       super().__init__("_revsurf_basic", {"point" : point, "path" : path, "coef" : coef, "neg" : neg, "maxdist" : maxdist, **kwargs})

class _revsurf_influence(_Bosl2Base):
    def __init__(self, point=None, path=None, coef=None, exp=None, neg=None, maxdist=None, **kwargs):
       super().__init__("_revsurf_influence", {"point" : point, "path" : path, "coef" : coef, "exp" : exp, "neg" : neg, "maxdist" : maxdist, **kwargs})

class _revsurf_cutoff(_Bosl2Base):
    def __init__(self, point=None, path=None, coef=None, cutoff=None, neg=None, maxdist=None, **kwargs):
       super().__init__("_revsurf_cutoff", {"point" : point, "path" : path, "coef" : coef, "cutoff" : cutoff, "neg" : neg, "maxdist" : maxdist, **kwargs})

class _revsurf_full(_Bosl2Base):
    def __init__(self, point=None, path=None, coef=None, cutoff=None, exp=None, neg=None, maxdist=None, **kwargs):
       super().__init__("_revsurf_full", {"point" : point, "path" : path, "coef" : coef, "cutoff" : cutoff, "exp" : exp, "neg" : neg, "maxdist" : maxdist, **kwargs})

class mb_cyl(_Bosl2Base):
    def __init__(self, h=None, r=None, rounding=None, r1=None, r2=None, l=None, height=None, length=None, d1=None, d2=None, d=None, cutoff=None, influence=None, negative=None, hide_debug=None, **kwargs):
       super().__init__("mb_cyl", {"h" : h, "r" : r, "rounding" : rounding, "r1" : r1, "r2" : r2, "l" : l, "height" : height, "length" : length, "d1" : d1, "d2" : d2, "d" : d, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, **kwargs})

class _mb_disk_basic(_Bosl2Base):
    def __init__(self, point=None, hl=None, r=None, neg=None, **kwargs):
       super().__init__("_mb_disk_basic", {"point" : point, "hl" : hl, "r" : r, "neg" : neg, **kwargs})

class _mb_disk_influence(_Bosl2Base):
    def __init__(self, point=None, hl=None, r=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_disk_influence", {"point" : point, "hl" : hl, "r" : r, "ex" : ex, "neg" : neg, **kwargs})

class _mb_disk_cutoff(_Bosl2Base):
    def __init__(self, point=None, hl=None, r=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_disk_cutoff", {"point" : point, "hl" : hl, "r" : r, "cutoff" : cutoff, "neg" : neg, **kwargs})

class _mb_disk_full(_Bosl2Base):
    def __init__(self, point=None, hl=None, r=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_disk_full", {"point" : point, "hl" : hl, "r" : r, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_disk(_Bosl2Base):
    def __init__(self, h=None, r=None, cutoff=None, influence=None, negative=None, hide_debug=None, d=None, l=None, height=None, length=None, **kwargs):
       super().__init__("mb_disk", {"h" : h, "r" : r, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d" : d, "l" : l, "height" : height, "length" : length, **kwargs})

class _mb_capsule_basic(_Bosl2Base):
    def __init__(self, dv=None, hl=None, r=None, neg=None, **kwargs):
       super().__init__("_mb_capsule_basic", {"dv" : dv, "hl" : hl, "r" : r, "neg" : neg, **kwargs})

class _mb_capsule_influence(_Bosl2Base):
    def __init__(self, dv=None, hl=None, r=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_capsule_influence", {"dv" : dv, "hl" : hl, "r" : r, "ex" : ex, "neg" : neg, **kwargs})

class _mb_capsule_cutoff(_Bosl2Base):
    def __init__(self, dv=None, hl=None, r=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_capsule_cutoff", {"dv" : dv, "hl" : hl, "r" : r, "cutoff" : cutoff, "neg" : neg, **kwargs})

class _mb_capsule_full(_Bosl2Base):
    def __init__(self, dv=None, hl=None, r=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_capsule_full", {"dv" : dv, "hl" : hl, "r" : r, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_capsule(_Bosl2Base):
    def __init__(self, h=None, r=None, cutoff=None, influence=None, negative=None, hide_debug=None, d=None, l=None, height=None, length=None, **kwargs):
       super().__init__("mb_capsule", {"h" : h, "r" : r, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d" : d, "l" : l, "height" : height, "length" : length, **kwargs})

class mb_connector(_Bosl2Base):
    def __init__(self, p1=None, p2=None, r=None, cutoff=None, influence=None, negative=None, hide_debug=None, d=None, **kwargs):
       super().__init__("mb_connector", {"p1" : p1, "p2" : p2, "r" : r, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d" : d, **kwargs})

class _mb_torus_basic(_Bosl2Base):
    def __init__(self, point=None, rmaj=None, rmin=None, neg=None, **kwargs):
       super().__init__("_mb_torus_basic", {"point" : point, "rmaj" : rmaj, "rmin" : rmin, "neg" : neg, **kwargs})

class _mb_torus_influence(_Bosl2Base):
    def __init__(self, point=None, rmaj=None, rmin=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_torus_influence", {"point" : point, "rmaj" : rmaj, "rmin" : rmin, "ex" : ex, "neg" : neg, **kwargs})

class _mb_torus_cutoff(_Bosl2Base):
    def __init__(self, point=None, rmaj=None, rmin=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_torus_cutoff", {"point" : point, "rmaj" : rmaj, "rmin" : rmin, "cutoff" : cutoff, "neg" : neg, **kwargs})

class _mb_torus_full(_Bosl2Base):
    def __init__(self, point=None, rmaj=None, rmin=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_torus_full", {"point" : point, "rmaj" : rmaj, "rmin" : rmin, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_torus(_Bosl2Base):
    def __init__(self, r_maj=None, r_min=None, cutoff=None, influence=None, negative=None, hide_debug=None, d_maj=None, d_min=None, _or=None, od=None, ir=None, id=None, **kwargs):
       super().__init__("mb_torus", {"r_maj" : r_maj, "r_min" : r_min, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d_maj" : d_maj, "d_min" : d_min, "_or" : _or, "od" : od, "ir" : ir, "id" : id, **kwargs})

class _mb_octahedron_basic(_Bosl2Base):
    def __init__(self, point=None, invr=None, xp=None, neg=None, **kwargs):
       super().__init__("_mb_octahedron_basic", {"point" : point, "invr" : invr, "xp" : xp, "neg" : neg, **kwargs})

class _mb_octahedron_influence(_Bosl2Base):
    def __init__(self, point=None, invr=None, xp=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_octahedron_influence", {"point" : point, "invr" : invr, "xp" : xp, "ex" : ex, "neg" : neg, **kwargs})

class _mb_octahedron_cutoff(_Bosl2Base):
    def __init__(self, point=None, invr=None, xp=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_octahedron_cutoff", {"point" : point, "invr" : invr, "xp" : xp, "cutoff" : cutoff, "neg" : neg, **kwargs})

class _mb_octahedron_full(_Bosl2Base):
    def __init__(self, point=None, invr=None, xp=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_octahedron_full", {"point" : point, "invr" : invr, "xp" : xp, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_octahedron(_Bosl2Base):
    def __init__(self, size=None, squareness=None, cutoff=None, influence=None, negative=None, hide_debug=None, **kwargs):
       super().__init__("mb_octahedron", {"size" : size, "squareness" : squareness, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, **kwargs})

class _debug_cube(_Bosl2Base):
    def __init__(self, size=None, squareness=None, **kwargs):
       super().__init__("_debug_cube", {"size" : size, "squareness" : squareness, **kwargs})

class _debug_octahedron(_Bosl2Base):
    def __init__(self, size=None, squareness=None, **kwargs):
       super().__init__("_debug_octahedron", {"size" : size, "squareness" : squareness, **kwargs})

class debug_tetra(_Bosl2Base):
    def __init__(self, r=None, **kwargs):
       super().__init__("debug_tetra", {"r" : r, **kwargs})

class metaballs(_Bosl2Base):
    def __init__(self, spec=None, bounding_box=None, voxel_size=None, voxel_count=None, isovalue=None, closed=None, exact_bounds=None, show_stats=None, _debug=None, **kwargs):
       super().__init__("metaballs", {"spec" : spec, "bounding_box" : bounding_box, "voxel_size" : voxel_size, "voxel_count" : voxel_count, "isovalue" : isovalue, "closed" : closed, "exact_bounds" : exact_bounds, "show_stats" : show_stats, "_debug" : _debug, **kwargs})

class _mb_unwind_list(_Bosl2Base):
    def __init__(self, list=None, parent_trans=None, depth=None, twoD=None, **kwargs):
       super().__init__("_mb_unwind_list", {"list" : list, "parent_trans" : parent_trans, "depth" : depth, "twoD" : twoD, **kwargs})

class _mb_circle_full(_Bosl2Base):
    def __init__(self, point=None, r=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_circle_full", {"point" : point, "r" : r, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_circle(_Bosl2Base):
    def __init__(self, r=None, cutoff=None, influence=None, negative=None, hide_debug=None, d=None, **kwargs):
       super().__init__("mb_circle", {"r" : r, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d" : d, **kwargs})

class _mb_squircle_full(_Bosl2Base):
    def __init__(self, point=None, inv_size=None, xp=None, ex=None, cutoff=None, neg=None, **kwargs):
       super().__init__("_mb_squircle_full", {"point" : point, "inv_size" : inv_size, "xp" : xp, "ex" : ex, "cutoff" : cutoff, "neg" : neg, **kwargs})

class mb_rect(_Bosl2Base):
    def __init__(self, size=None, squareness=None, cutoff=None, influence=None, negative=None, hide_debug=None, **kwargs):
       super().__init__("mb_rect", {"size" : size, "squareness" : squareness, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, **kwargs})

class _trapsurf_full(_Bosl2Base):
    def __init__(self, point=None, path=None, coef=None, cutoff=None, exp=None, neg=None, maxdist=None, **kwargs):
       super().__init__("_trapsurf_full", {"point" : point, "path" : path, "coef" : coef, "cutoff" : cutoff, "exp" : exp, "neg" : neg, "maxdist" : maxdist, **kwargs})

class mb_trapezoid(_Bosl2Base):
    def __init__(self, h=None, w1=None, w2=None, ang=None, rounding=None, w=None, cutoff=None, influence=None, negative=None, hide_debug=None, **kwargs):
       super().__init__("mb_trapezoid", {"h" : h, "w1" : w1, "w2" : w2, "ang" : ang, "rounding" : rounding, "w" : w, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, **kwargs})

class _mb_stadium_full(_Bosl2Base):
    def __init__(self, dv=None, hl=None, r=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_stadium_full", {"dv" : dv, "hl" : hl, "r" : r, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class _mb_stadium_sideways_full(_Bosl2Base):
    def __init__(self, dv=None, hl=None, r=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_stadium_sideways_full", {"dv" : dv, "hl" : hl, "r" : r, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_stadium(_Bosl2Base):
    def __init__(self, size=None, cutoff=None, influence=None, negative=None, hide_debug=None, **kwargs):
       super().__init__("mb_stadium", {"size" : size, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, **kwargs})

class mb_connector2d(_Bosl2Base):
    def __init__(self, p1=None, p2=None, r=None, cutoff=None, influence=None, negative=None, hide_debug=None, d=None, **kwargs):
       super().__init__("mb_connector2d", {"p1" : p1, "p2" : p2, "r" : r, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d" : d, **kwargs})

class _mb_ring_full(_Bosl2Base):
    def __init__(self, point=None, rmaj=None, rmin=None, cutoff=None, ex=None, neg=None, **kwargs):
       super().__init__("_mb_ring_full", {"point" : point, "rmaj" : rmaj, "rmin" : rmin, "cutoff" : cutoff, "ex" : ex, "neg" : neg, **kwargs})

class mb_ring(_Bosl2Base):
    def __init__(self, r1=None, r2=None, cutoff=None, influence=None, negative=None, hide_debug=None, d1=None, d2=None, **kwargs):
       super().__init__("mb_ring", {"r1" : r1, "r2" : r2, "cutoff" : cutoff, "influence" : influence, "negative" : negative, "hide_debug" : hide_debug, "d1" : d1, "d2" : d2, **kwargs})

class metaballs2d(_Bosl2Base):
    def __init__(self, spec=None, bounding_box=None, pixel_size=None, pixel_count=None, isovalue=None, closed=None, use_centers=None, smoothing=None, exact_bounds=None, show_stats=None, _debug=None, **kwargs):
       super().__init__("metaballs2d", {"spec" : spec, "bounding_box" : bounding_box, "pixel_size" : pixel_size, "pixel_count" : pixel_count, "isovalue" : isovalue, "closed" : closed, "use_centers" : use_centers, "smoothing" : smoothing, "exact_bounds" : exact_bounds, "show_stats" : show_stats, "_debug" : _debug, **kwargs})

class _metaballs2dfield(_Bosl2Base):
    def __init__(self, funclist=None, transmatrix=None, bbox=None, pixsize=None, nballs=None, **kwargs):
       super().__init__("_metaballs2dfield", {"funclist" : funclist, "transmatrix" : transmatrix, "bbox" : bbox, "pixsize" : pixsize, "nballs" : nballs, **kwargs})

class isosurface(_Bosl2Base):
    def __init__(self, f=None, isovalue=None, bounding_box=None, voxel_size=None, voxel_count=None, reverse=None, closed=None, exact_bounds=None, show_stats=None, _mball=None, **kwargs):
       super().__init__("isosurface", {"f" : f, "isovalue" : isovalue, "bounding_box" : bounding_box, "voxel_size" : voxel_size, "voxel_count" : voxel_count, "reverse" : reverse, "closed" : closed, "exact_bounds" : exact_bounds, "show_stats" : show_stats, "_mball" : _mball, **kwargs})

class _getautovoxsize(_Bosl2Base):
    def __init__(self, bbox=None, numvoxels=None, **kwargs):
       super().__init__("_getautovoxsize", {"bbox" : bbox, "numvoxels" : numvoxels, **kwargs})

class _getvoxsize(_Bosl2Base):
    def __init__(self, voxel_size=None, bounding_box=None, exactbounds=None, **kwargs):
       super().__init__("_getvoxsize", {"voxel_size" : voxel_size, "bounding_box" : bounding_box, "exactbounds" : exactbounds, **kwargs})

class _getbbox(_Bosl2Base):
    def __init__(self, voxel_size=None, bounding_box=None, exactbounds=None, f=None, **kwargs):
       super().__init__("_getbbox", {"voxel_size" : voxel_size, "bounding_box" : bounding_box, "exactbounds" : exactbounds, "f" : f, **kwargs})

class _showstats_isosurface(_Bosl2Base):
    def __init__(self, voxsize=None, bbox=None, isoval=None, cubes=None, triangles=None, faces=None, **kwargs):
       super().__init__("_showstats_isosurface", {"voxsize" : voxsize, "bbox" : bbox, "isoval" : isoval, "cubes" : cubes, "triangles" : triangles, "faces" : faces, **kwargs})

class contour(_Bosl2Base):
    def __init__(self, f=None, isovalue=None, bounding_box=None, pixel_size=None, pixel_count=None, use_centers=None, smoothing=None, closed=None, exact_bounds=None, show_stats=None, _mball=None, **kwargs):
       super().__init__("contour", {"f" : f, "isovalue" : isovalue, "bounding_box" : bounding_box, "pixel_size" : pixel_size, "pixel_count" : pixel_count, "use_centers" : use_centers, "smoothing" : smoothing, "closed" : closed, "exact_bounds" : exact_bounds, "show_stats" : show_stats, "_mball" : _mball, **kwargs})

class _region_smooth(_Bosl2Base):
    def __init__(self, reg=None, passes=None, bbox=None, count=None, **kwargs):
       super().__init__("_region_smooth", {"reg" : reg, "passes" : passes, "bbox" : bbox, "count" : count, **kwargs})

class _is_pt_on_bbox(_Bosl2Base):
    def __init__(self, p=None, bbox=None, **kwargs):
       super().__init__("_is_pt_on_bbox", {"p" : p, "bbox" : bbox, **kwargs})

class _pathpts_on_bbox(_Bosl2Base):
    def __init__(self, path=None, bbox=None, i=None, count=None, **kwargs):
       super().__init__("_pathpts_on_bbox", {"path" : path, "bbox" : bbox, "i" : i, "count" : count, **kwargs})

class _getautopixsize(_Bosl2Base):
    def __init__(self, bbox=None, numpixels=None, **kwargs):
       super().__init__("_getautopixsize", {"bbox" : bbox, "numpixels" : numpixels, **kwargs})

class _getpixsize(_Bosl2Base):
    def __init__(self, pixel_size=None, bounding_box=None, exactbounds=None, **kwargs):
       super().__init__("_getpixsize", {"pixel_size" : pixel_size, "bounding_box" : bounding_box, "exactbounds" : exactbounds, **kwargs})

class _getbbox2d(_Bosl2Base):
    def __init__(self, pixel_size=None, bounding_box=None, exactbounds=None, f=None, **kwargs):
       super().__init__("_getbbox2d", {"pixel_size" : pixel_size, "bounding_box" : bounding_box, "exactbounds" : exactbounds, "f" : f, **kwargs})

class _showstats_contour(_Bosl2Base):
    def __init__(self, pixelsize=None, bbox=None, isovalmin=None, isovalmax=None, pixels=None, pathlist=None, **kwargs):
       super().__init__("_showstats_contour", {"pixelsize" : pixelsize, "bbox" : bbox, "isovalmin" : isovalmin, "isovalmax" : isovalmax, "pixels" : pixels, "pathlist" : pathlist, **kwargs})

class metaballs(_Bosl2Base):
    def __init__(self, spec=None, bounding_box=None, voxel_size=None, voxel_count=None, isovalue=None, closed=None, exact_bounds=None, convexity=None, cp=None, anchor=None, spin=None, orient=None, atype=None, show_stats=None, show_box=None, debug=None, **kwargs):
       super().__init__("metaballs", {"spec" : spec, "bounding_box" : bounding_box, "voxel_size" : voxel_size, "voxel_count" : voxel_count, "isovalue" : isovalue, "closed" : closed, "exact_bounds" : exact_bounds, "convexity" : convexity, "cp" : cp, "anchor" : anchor, "spin" : spin, "orient" : orient, "atype" : atype, "show_stats" : show_stats, "show_box" : show_box, "debug" : debug, **kwargs})

class metaballs2d(_Bosl2Base):
    def __init__(self, spec=None, bounding_box=None, pixel_size=None, pixel_count=None, isovalue=None, use_centers=None, smoothing=None, exact_bounds=None, convexity=None, cp=None, anchor=None, spin=None, atype=None, show_stats=None, show_box=None, debug=None, **kwargs):
       super().__init__("metaballs2d", {"spec" : spec, "bounding_box" : bounding_box, "pixel_size" : pixel_size, "pixel_count" : pixel_count, "isovalue" : isovalue, "use_centers" : use_centers, "smoothing" : smoothing, "exact_bounds" : exact_bounds, "convexity" : convexity, "cp" : cp, "anchor" : anchor, "spin" : spin, "atype" : atype, "show_stats" : show_stats, "show_box" : show_box, "debug" : debug, **kwargs})

class isosurface(_Bosl2Base):
    def __init__(self, f=None, isovalue=None, bounding_box=None, voxel_size=None, voxel_count=None, reverse=None, closed=None, exact_bounds=None, convexity=None, cp=None, anchor=None, spin=None, orient=None, atype=None, show_stats=None, show_box=None, _mball=None, **kwargs):
       super().__init__("isosurface", {"f" : f, "isovalue" : isovalue, "bounding_box" : bounding_box, "voxel_size" : voxel_size, "voxel_count" : voxel_count, "reverse" : reverse, "closed" : closed, "exact_bounds" : exact_bounds, "convexity" : convexity, "cp" : cp, "anchor" : anchor, "spin" : spin, "orient" : orient, "atype" : atype, "show_stats" : show_stats, "show_box" : show_box, "_mball" : _mball, **kwargs})

class contour(_Bosl2Base):
    def __init__(self, f=None, isovalue=None, bounding_box=None, pixel_size=None, pixel_count=None, use_centers=None, smoothing=None, exact_bounds=None, cp=None, anchor=None, spin=None, atype=None, show_stats=None, show_box=None, _mball=None, **kwargs):
       super().__init__("contour", {"f" : f, "isovalue" : isovalue, "bounding_box" : bounding_box, "pixel_size" : pixel_size, "pixel_count" : pixel_count, "use_centers" : use_centers, "smoothing" : smoothing, "exact_bounds" : exact_bounds, "cp" : cp, "anchor" : anchor, "spin" : spin, "atype" : atype, "show_stats" : show_stats, "show_box" : show_box, "_mball" : _mball, **kwargs})

