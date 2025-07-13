from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/constants.scad'}", False)

_UNDEF = _OpenSCADConstant('_UNDEF')
INCH = _OpenSCADConstant('INCH')
IDENT = _OpenSCADConstant('IDENT')
LEFT = _OpenSCADConstant('LEFT')
RIGHT = _OpenSCADConstant('RIGHT')
FRONT = _OpenSCADConstant('FRONT')
FWD = _OpenSCADConstant('FWD')
FORWARD = _OpenSCADConstant('FORWARD')
BACK = _OpenSCADConstant('BACK')
BOTTOM = _OpenSCADConstant('BOTTOM')
BOT = _OpenSCADConstant('BOT')
DOWN = _OpenSCADConstant('DOWN')
TOP = _OpenSCADConstant('TOP')
UP = _OpenSCADConstant('UP')
CENTER = _OpenSCADConstant('CENTER')
CTR = _OpenSCADConstant('CTR')
CENTRE = _OpenSCADConstant('CENTRE')
SEGMENT = _OpenSCADConstant('SEGMENT')
RAY = _OpenSCADConstant('RAY')
LINE = _OpenSCADConstant('LINE')
class get_slop(_Bosl2Base):
    def __init__(self, **kwargs):
       super().__init__("get_slop", {**kwargs})

class EDGE(_Bosl2Base):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("EDGE", {"a" : a, "b" : b, **kwargs})

class FACE(_Bosl2Base):
    def __init__(self, i=None, **kwargs):
       super().__init__("FACE", {"i" : i, **kwargs})

