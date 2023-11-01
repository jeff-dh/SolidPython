from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/modular_hose.scad'}", False)

_modhose_small_end = _OpenSCADConstant('_modhose_small_end')
_modhose_big_end = _OpenSCADConstant('_modhose_big_end')
_modhose_waist = _OpenSCADConstant('_modhose_waist')
class modular_hose(_Bosl2Base):
    def __init__(self, size=None, type=None, clearance=None, waist_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("modular_hose", {"size" : size, "type" : type, "clearance" : clearance, "waist_len" : waist_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class modular_hose_radius(_Bosl2Base):
    def __init__(self, size=None, outer=None, **kwargs):
       super().__init__("modular_hose_radius", {"size" : size, "outer" : outer, **kwargs})

class modular_hose(_Bosl2Base):
    def __init__(self, size=None, type=None, clearance=None, waist_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("modular_hose", {"size" : size, "type" : type, "clearance" : clearance, "waist_len" : waist_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

