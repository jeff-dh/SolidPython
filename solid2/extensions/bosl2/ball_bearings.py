from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/ball_bearings.scad'}", False)

class ball_bearing_info(_Bosl2Base):
    def __init__(self, trade_size=None, **kwargs):
       super().__init__("ball_bearing_info", {"trade_size" : trade_size, **kwargs})

class ball_bearing(_Bosl2Base):
    def __init__(self, trade_size=None, id=None, od=None, width=None, shield=None, flange=None, fd=None, fw=None, rounding=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ball_bearing", {"trade_size" : trade_size, "id" : id, "od" : od, "width" : width, "shield" : shield, "flange" : flange, "fd" : fd, "fw" : fw, "rounding" : rounding, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

