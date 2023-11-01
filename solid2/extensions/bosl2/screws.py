from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/screws.scad'}", False)

class _get_spec(_Bosl2Base):
    def __init__(self, spec=None, needtype=None, origin=None, thread=None, head=None, drive=None, drive_size=None, shape=None, thickness=None, **kwargs):
       super().__init__("_get_spec", {"spec" : spec, "needtype" : needtype, "origin" : origin, "thread" : thread, "head" : head, "drive" : drive, "drive_size" : drive_size, "shape" : shape, "thickness" : thickness, **kwargs})

class _struct_reset(_Bosl2Base):
    def __init__(self, s=None, keyval=None, grow=None, **kwargs):
       super().__init__("_struct_reset", {"s" : s, "keyval" : keyval, "grow" : grow, **kwargs})

class _nominal_diam(_Bosl2Base):
    def __init__(self, spec=None, **kwargs):
       super().__init__("_nominal_diam", {"spec" : spec, **kwargs})

class screw(_Bosl2Base):
    def __init__(self, spec=None, head=None, drive=None, thread=None, drive_size=None, length=None, l=None, thread_len=None, tolerance=None, details=None, undersize=None, shaft_undersize=None, head_undersize=None, atype=None, anchor=None, spin=None, orient=None, _shoulder_diam=None, _shoulder_len=None, bevel=None, bevel1=None, bevel2=None, bevelsize=None, blunt_start=None, blunt_start1=None, blunt_start2=None, _internal=None, _counterbore=None, _teardrop=None, **kwargs):
       super().__init__("screw", {"spec" : spec, "head" : head, "drive" : drive, "thread" : thread, "drive_size" : drive_size, "length" : length, "l" : l, "thread_len" : thread_len, "tolerance" : tolerance, "details" : details, "undersize" : undersize, "shaft_undersize" : shaft_undersize, "head_undersize" : head_undersize, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, "_shoulder_diam" : _shoulder_diam, "_shoulder_len" : _shoulder_len, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevelsize" : bevelsize, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "_internal" : _internal, "_counterbore" : _counterbore, "_teardrop" : _teardrop, **kwargs})

class screw_hole(_Bosl2Base):
    def __init__(self, spec=None, head=None, thread=None, oversize=None, hole_oversize=None, head_oversize=None, length=None, l=None, thread_len=None, tolerance=None, counterbore=None, teardrop=None, bevel=None, bevel1=None, bevel2=None, blunt_start=None, blunt_start1=None, blunt_start2=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("screw_hole", {"spec" : spec, "head" : head, "thread" : thread, "oversize" : oversize, "hole_oversize" : hole_oversize, "head_oversize" : head_oversize, "length" : length, "l" : l, "thread_len" : thread_len, "tolerance" : tolerance, "counterbore" : counterbore, "teardrop" : teardrop, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class shoulder_screw(_Bosl2Base):
    def __init__(self, s=None, d=None, length=None, head=None, thread_len=None, tolerance=None, head_size=None, drive=None, drive_size=None, thread=None, undersize=None, shaft_undersize=None, head_undersize=None, shoulder_undersize=None, blunt_start=None, blunt_start1=None, blunt_start2=None, atype=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("shoulder_screw", {"s" : s, "d" : d, "length" : length, "head" : head, "thread_len" : thread_len, "tolerance" : tolerance, "head_size" : head_size, "drive" : drive, "drive_size" : drive_size, "thread" : thread, "undersize" : undersize, "shaft_undersize" : shaft_undersize, "head_undersize" : head_undersize, "shoulder_undersize" : shoulder_undersize, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "atype" : atype, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})

class _ISO_thread_tolerance(_Bosl2Base):
    def __init__(self, diameter=None, pitch=None, internal=None, tolerance=None, **kwargs):
       super().__init__("_ISO_thread_tolerance", {"diameter" : diameter, "pitch" : pitch, "internal" : internal, "tolerance" : tolerance, **kwargs})

class _UTS_thread_tolerance(_Bosl2Base):
    def __init__(self, diam=None, pitch=None, internal=None, tolerance=None, **kwargs):
       super().__init__("_UTS_thread_tolerance", {"diam" : diam, "pitch" : pitch, "internal" : internal, "tolerance" : tolerance, **kwargs})

class _exact_thread_tolerance(_Bosl2Base):
    def __init__(self, d=None, P=None, **kwargs):
       super().__init__("_exact_thread_tolerance", {"d" : d, "P" : P, **kwargs})

class _parse_screw_name(_Bosl2Base):
    def __init__(self, name=None, **kwargs):
       super().__init__("_parse_screw_name", {"name" : name, **kwargs})

class _parse_drive(_Bosl2Base):
    def __init__(self, drive=None, drive_size=None, **kwargs):
       super().__init__("_parse_drive", {"drive" : drive, "drive_size" : drive_size, **kwargs})

class screw_head(_Bosl2Base):
    def __init__(self, screw_info=None, details=None, counterbore=None, flat_height=None, teardrop=None, slop=None, **kwargs):
       super().__init__("screw_head", {"screw_info" : screw_info, "details" : details, "counterbore" : counterbore, "flat_height" : flat_height, "teardrop" : teardrop, "slop" : slop, **kwargs})

class nut(_Bosl2Base):
    def __init__(self, spec=None, shape=None, thickness=None, nutwidth=None, thread=None, tolerance=None, hole_oversize=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, blunt_start=None, blunt_start1=None, blunt_start2=None, anchor=None, spin=None, orient=None, oversize=None, **kwargs):
       super().__init__("nut", {"spec" : spec, "shape" : shape, "thickness" : thickness, "nutwidth" : nutwidth, "thread" : thread, "tolerance" : tolerance, "hole_oversize" : hole_oversize, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "anchor" : anchor, "spin" : spin, "orient" : orient, "oversize" : oversize, **kwargs})

class screw_info(_Bosl2Base):
    def __init__(self, name=None, head=None, drive=None, thread=None, drive_size=None, shaft_oversize=None, head_oversize=None, _origin=None, **kwargs):
       super().__init__("screw_info", {"name" : name, "head" : head, "drive" : drive, "thread" : thread, "drive_size" : drive_size, "shaft_oversize" : shaft_oversize, "head_oversize" : head_oversize, "_origin" : _origin, **kwargs})

class nut_info(_Bosl2Base):
    def __init__(self, name=None, shape=None, thickness=None, thread=None, hole_oversize=None, width=None, _origin=None, **kwargs):
       super().__init__("nut_info", {"name" : name, "shape" : shape, "thickness" : thickness, "thread" : thread, "hole_oversize" : hole_oversize, "width" : width, "_origin" : _origin, **kwargs})

class _nut_info_english(_Bosl2Base):
    def __init__(self, diam=None, threadcount=None, thread=None, shape=None, thickness=None, width=None, **kwargs):
       super().__init__("_nut_info_english", {"diam" : diam, "threadcount" : threadcount, "thread" : thread, "shape" : shape, "thickness" : thickness, "width" : width, **kwargs})

class _downcase_if_str(_Bosl2Base):
    def __init__(self, s=None, **kwargs):
       super().__init__("_downcase_if_str", {"s" : s, **kwargs})

class _nut_info_metric(_Bosl2Base):
    def __init__(self, diam=None, pitch=None, thread=None, shape=None, thickness=None, width=None, **kwargs):
       super().__init__("_nut_info_metric", {"diam" : diam, "pitch" : pitch, "thread" : thread, "shape" : shape, "thickness" : thickness, "width" : width, **kwargs})

class _screw_info_english(_Bosl2Base):
    def __init__(self, diam=None, threadcount=None, head=None, thread=None, drive=None, **kwargs):
       super().__init__("_screw_info_english", {"diam" : diam, "threadcount" : threadcount, "head" : head, "thread" : thread, "drive" : drive, **kwargs})

class _screw_info_metric(_Bosl2Base):
    def __init__(self, diam=None, pitch=None, head=None, thread=None, drive=None, **kwargs):
       super().__init__("_screw_info_metric", {"diam" : diam, "pitch" : pitch, "head" : head, "thread" : thread, "drive" : drive, **kwargs})

class _is_positive(_Bosl2Base):
    def __init__(self, x=None, **kwargs):
       super().__init__("_is_positive", {"x" : x, **kwargs})

class _validate_nut_spec(_Bosl2Base):
    def __init__(self, spec=None, **kwargs):
       super().__init__("_validate_nut_spec", {"spec" : spec, **kwargs})

class _validate_screw_spec(_Bosl2Base):
    def __init__(self, spec=None, **kwargs):
       super().__init__("_validate_screw_spec", {"spec" : spec, **kwargs})

class thread_specification(_Bosl2Base):
    def __init__(self, screw_spec=None, tolerance=None, internal=None, **kwargs):
       super().__init__("thread_specification", {"screw_spec" : screw_spec, "tolerance" : tolerance, "internal" : internal, **kwargs})

class screw(_Bosl2Base):
    def __init__(self, spec=None, head=None, drive=None, thread=None, drive_size=None, length=None, l=None, thread_len=None, tolerance=None, details=None, undersize=None, shaft_undersize=None, head_undersize=None, atype=None, anchor=None, spin=None, orient=None, _shoulder_diam=None, _shoulder_len=None, bevel=None, bevel1=None, bevel2=None, bevelsize=None, blunt_start=None, blunt_start1=None, blunt_start2=None, _internal=None, _counterbore=None, _teardrop=None, **kwargs):
       super().__init__("screw", {"spec" : spec, "head" : head, "drive" : drive, "thread" : thread, "drive_size" : drive_size, "length" : length, "l" : l, "thread_len" : thread_len, "tolerance" : tolerance, "details" : details, "undersize" : undersize, "shaft_undersize" : shaft_undersize, "head_undersize" : head_undersize, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, "_shoulder_diam" : _shoulder_diam, "_shoulder_len" : _shoulder_len, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevelsize" : bevelsize, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "_internal" : _internal, "_counterbore" : _counterbore, "_teardrop" : _teardrop, **kwargs})

class screw_hole(_Bosl2Base):
    def __init__(self, spec=None, head=None, thread=None, oversize=None, hole_oversize=None, head_oversize=None, length=None, l=None, thread_len=None, tolerance=None, counterbore=None, teardrop=None, bevel=None, bevel1=None, bevel2=None, blunt_start=None, blunt_start1=None, blunt_start2=None, atype=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("screw_hole", {"spec" : spec, "head" : head, "thread" : thread, "oversize" : oversize, "hole_oversize" : hole_oversize, "head_oversize" : head_oversize, "length" : length, "l" : l, "thread_len" : thread_len, "tolerance" : tolerance, "counterbore" : counterbore, "teardrop" : teardrop, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "atype" : atype, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class shoulder_screw(_Bosl2Base):
    def __init__(self, s=None, d=None, length=None, head=None, thread_len=None, tolerance=None, head_size=None, drive=None, drive_size=None, thread=None, undersize=None, shaft_undersize=None, head_undersize=None, shoulder_undersize=None, blunt_start=None, blunt_start1=None, blunt_start2=None, atype=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("shoulder_screw", {"s" : s, "d" : d, "length" : length, "head" : head, "thread_len" : thread_len, "tolerance" : tolerance, "head_size" : head_size, "drive" : drive, "drive_size" : drive_size, "thread" : thread, "undersize" : undersize, "shaft_undersize" : shaft_undersize, "head_undersize" : head_undersize, "shoulder_undersize" : shoulder_undersize, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "atype" : atype, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})

class _driver(_Bosl2Base):
    def __init__(self, spec=None, **kwargs):
       super().__init__("_driver", {"spec" : spec, **kwargs})

class screw_head(_Bosl2Base):
    def __init__(self, screw_info=None, details=None, counterbore=None, flat_height=None, teardrop=None, slop=None, **kwargs):
       super().__init__("screw_head", {"screw_info" : screw_info, "details" : details, "counterbore" : counterbore, "flat_height" : flat_height, "teardrop" : teardrop, "slop" : slop, **kwargs})

class nut(_Bosl2Base):
    def __init__(self, spec=None, shape=None, thickness=None, nutwidth=None, thread=None, tolerance=None, hole_oversize=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, blunt_start=None, blunt_start1=None, blunt_start2=None, anchor=None, spin=None, orient=None, oversize=None, **kwargs):
       super().__init__("nut", {"spec" : spec, "shape" : shape, "thickness" : thickness, "nutwidth" : nutwidth, "thread" : thread, "tolerance" : tolerance, "hole_oversize" : hole_oversize, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "anchor" : anchor, "spin" : spin, "orient" : orient, "oversize" : oversize, **kwargs})

class nut_trap_side(_Bosl2Base):
    def __init__(self, trap_width=None, spec=None, shape=None, thickness=None, nutwidth=None, anchor=None, orient=None, spin=None, poke_len=None, poke_diam=None, **kwargs):
       super().__init__("nut_trap_side", {"trap_width" : trap_width, "spec" : spec, "shape" : shape, "thickness" : thickness, "nutwidth" : nutwidth, "anchor" : anchor, "orient" : orient, "spin" : spin, "poke_len" : poke_len, "poke_diam" : poke_diam, **kwargs})

class nut_trap_inline(_Bosl2Base):
    def __init__(self, length=None, spec=None, shape=None, l=None, height=None, h=None, nutwidth=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("nut_trap_inline", {"length" : length, "spec" : spec, "shape" : shape, "l" : l, "height" : height, "h" : h, "nutwidth" : nutwidth, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})

