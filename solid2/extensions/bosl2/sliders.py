from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/sliders.scad'}", False)

class slider(_Bosl2Base):
    def __init__(self, l=None, w=None, h=None, base=None, wall=None, ang=None, chamfer=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("slider", {"l" : l, "w" : w, "h" : h, "base" : base, "wall" : wall, "ang" : ang, "chamfer" : chamfer, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rail(_Bosl2Base):
    def __init__(self, l=None, w=None, h=None, chamfer=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rail", {"l" : l, "w" : w, "h" : h, "chamfer" : chamfer, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class slider(_Bosl2Base):
    def __init__(self, l=None, w=None, h=None, base=None, wall=None, ang=None, chamfer=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("slider", {"l" : l, "w" : w, "h" : h, "base" : base, "wall" : wall, "ang" : ang, "chamfer" : chamfer, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rail(_Bosl2Base):
    def __init__(self, l=None, w=None, h=None, chamfer=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rail", {"l" : l, "w" : w, "h" : h, "chamfer" : chamfer, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

