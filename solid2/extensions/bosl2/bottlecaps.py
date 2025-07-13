from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/bottlecaps.scad'}", False)

_sp_specs = _OpenSCADConstant('_sp_specs')
_sp_twist = _OpenSCADConstant('_sp_twist')
_sp_thread_width = _OpenSCADConstant('_sp_thread_width')
class pco1810_neck(_Bosl2Base):
    def __init__(self, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1810_neck", {"wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pco1810_cap(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, wall=None, texture=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1810_cap", {"h" : h, "r" : r, "d" : d, "wall" : wall, "texture" : texture, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pco1881_neck(_Bosl2Base):
    def __init__(self, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1881_neck", {"wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pco1881_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1881_cap", {"wall" : wall, "texture" : texture, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_bottle_neck(_Bosl2Base):
    def __init__(self, neck_d=None, id=None, thread_od=None, height=None, support_d=None, pitch=None, round_supp=None, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_bottle_neck", {"neck_d" : neck_d, "id" : id, "thread_od" : thread_od, "height" : height, "support_d" : support_d, "pitch" : pitch, "round_supp" : round_supp, "wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_bottle_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, height=None, thread_od=None, tolerance=None, neck_od=None, flank_angle=None, pitch=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_bottle_cap", {"wall" : wall, "texture" : texture, "height" : height, "thread_od" : thread_od, "tolerance" : tolerance, "neck_od" : neck_od, "flank_angle" : flank_angle, "pitch" : pitch, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class bottle_adapter_neck_to_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, cap_wall=None, cap_h=None, cap_thread_depth1=None, tolerance=None, cap_neck_od=None, cap_neck_id=None, cap_thread_taper=None, cap_thread_pitch=None, neck_d=None, neck_id=None, neck_thread_od=None, neck_h=None, neck_thread_pitch=None, neck_support_od=None, d=None, taper_lead_in=None, **kwargs):
       super().__init__("bottle_adapter_neck_to_cap", {"wall" : wall, "texture" : texture, "cap_wall" : cap_wall, "cap_h" : cap_h, "cap_thread_depth1" : cap_thread_depth1, "tolerance" : tolerance, "cap_neck_od" : cap_neck_od, "cap_neck_id" : cap_neck_id, "cap_thread_taper" : cap_thread_taper, "cap_thread_pitch" : cap_thread_pitch, "neck_d" : neck_d, "neck_id" : neck_id, "neck_thread_od" : neck_thread_od, "neck_h" : neck_h, "neck_thread_pitch" : neck_thread_pitch, "neck_support_od" : neck_support_od, "d" : d, "taper_lead_in" : taper_lead_in, **kwargs})

class bottle_adapter_cap_to_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, cap_h1=None, cap_thread_od1=None, tolerance=None, cap_neck_od1=None, cap_thread_pitch1=None, cap_h2=None, cap_thread_od2=None, cap_neck_od2=None, cap_thread_pitch2=None, d=None, neck_id1=None, neck_id2=None, taper_lead_in=None, **kwargs):
       super().__init__("bottle_adapter_cap_to_cap", {"wall" : wall, "texture" : texture, "cap_h1" : cap_h1, "cap_thread_od1" : cap_thread_od1, "tolerance" : tolerance, "cap_neck_od1" : cap_neck_od1, "cap_thread_pitch1" : cap_thread_pitch1, "cap_h2" : cap_h2, "cap_thread_od2" : cap_thread_od2, "cap_neck_od2" : cap_neck_od2, "cap_thread_pitch2" : cap_thread_pitch2, "d" : d, "neck_id1" : neck_id1, "neck_id2" : neck_id2, "taper_lead_in" : taper_lead_in, **kwargs})

class bottle_adapter_neck_to_neck(_Bosl2Base):
    def __init__(self, d=None, neck_od1=None, neck_id1=None, thread_od1=None, height1=None, support_od1=None, thread_pitch1=None, neck_od2=None, neck_id2=None, thread_od2=None, height2=None, support_od2=None, pitch2=None, taper_lead_in=None, wall=None, **kwargs):
       super().__init__("bottle_adapter_neck_to_neck", {"d" : d, "neck_od1" : neck_od1, "neck_id1" : neck_id1, "thread_od1" : thread_od1, "height1" : height1, "support_od1" : support_od1, "thread_pitch1" : thread_pitch1, "neck_od2" : neck_od2, "neck_id2" : neck_id2, "thread_od2" : thread_od2, "height2" : height2, "support_od2" : support_od2, "pitch2" : pitch2, "taper_lead_in" : taper_lead_in, "wall" : wall, **kwargs})

class _sp_thread_profile(_Bosl2Base):
    def __init__(self, tpi=None, a=None, S=None, style=None, flip=None, **kwargs):
       super().__init__("_sp_thread_profile", {"tpi" : tpi, "a" : a, "S" : S, "style" : style, "flip" : flip, **kwargs})

class sp_neck(_Bosl2Base):
    def __init__(self, diam=None, type=None, wall=None, id=None, style=None, bead=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sp_neck", {"diam" : diam, "type" : type, "wall" : wall, "id" : id, "style" : style, "bead" : bead, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sp_diameter(_Bosl2Base):
    def __init__(self, diam=None, type=None, **kwargs):
       super().__init__("sp_diameter", {"diam" : diam, "type" : type, **kwargs})

class pco1810_neck(_Bosl2Base):
    def __init__(self, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1810_neck", {"wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pco1810_cap(_Bosl2Base):
    def __init__(self, h=None, r=None, d=None, wall=None, texture=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1810_cap", {"h" : h, "r" : r, "d" : d, "wall" : wall, "texture" : texture, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pco1881_neck(_Bosl2Base):
    def __init__(self, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1881_neck", {"wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pco1881_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pco1881_cap", {"wall" : wall, "texture" : texture, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_bottle_neck(_Bosl2Base):
    def __init__(self, wall=None, neck_d=None, id=None, thread_od=None, height=None, support_d=None, pitch=None, round_supp=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_bottle_neck", {"wall" : wall, "neck_d" : neck_d, "id" : id, "thread_od" : thread_od, "height" : height, "support_d" : support_d, "pitch" : pitch, "round_supp" : round_supp, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_bottle_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, height=None, thread_depth=None, thread_od=None, tolerance=None, neck_od=None, flank_angle=None, pitch=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_bottle_cap", {"wall" : wall, "texture" : texture, "height" : height, "thread_depth" : thread_depth, "thread_od" : thread_od, "tolerance" : tolerance, "neck_od" : neck_od, "flank_angle" : flank_angle, "pitch" : pitch, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class bottle_adapter_neck_to_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, cap_wall=None, cap_h=None, cap_thread_depth=None, tolerance=None, cap_neck_od=None, cap_neck_id=None, cap_thread_taper=None, cap_thread_pitch=None, neck_d=None, neck_id=None, neck_thread_od=None, neck_h=None, neck_thread_pitch=None, neck_support_od=None, d=None, taper_lead_in=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("bottle_adapter_neck_to_cap", {"wall" : wall, "texture" : texture, "cap_wall" : cap_wall, "cap_h" : cap_h, "cap_thread_depth" : cap_thread_depth, "tolerance" : tolerance, "cap_neck_od" : cap_neck_od, "cap_neck_id" : cap_neck_id, "cap_thread_taper" : cap_thread_taper, "cap_thread_pitch" : cap_thread_pitch, "neck_d" : neck_d, "neck_id" : neck_id, "neck_thread_od" : neck_thread_od, "neck_h" : neck_h, "neck_thread_pitch" : neck_thread_pitch, "neck_support_od" : neck_support_od, "d" : d, "taper_lead_in" : taper_lead_in, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class bottle_adapter_cap_to_cap(_Bosl2Base):
    def __init__(self, wall=None, texture=None, cap_h1=None, cap_thread_depth1=None, tolerance=None, cap_neck_od1=None, cap_thread_pitch1=None, cap_h2=None, cap_thread_depth2=None, cap_neck_od2=None, cap_thread_pitch2=None, d=None, neck_id=None, taper_lead_in=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("bottle_adapter_cap_to_cap", {"wall" : wall, "texture" : texture, "cap_h1" : cap_h1, "cap_thread_depth1" : cap_thread_depth1, "tolerance" : tolerance, "cap_neck_od1" : cap_neck_od1, "cap_thread_pitch1" : cap_thread_pitch1, "cap_h2" : cap_h2, "cap_thread_depth2" : cap_thread_depth2, "cap_neck_od2" : cap_neck_od2, "cap_thread_pitch2" : cap_thread_pitch2, "d" : d, "neck_id" : neck_id, "taper_lead_in" : taper_lead_in, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class bottle_adapter_neck_to_neck(_Bosl2Base):
    def __init__(self, d=None, neck_od1=None, neck_id1=None, thread_od1=None, height1=None, support_od1=None, thread_pitch1=None, neck_od2=None, neck_id2=None, thread_od2=None, height2=None, support_od2=None, pitch2=None, taper_lead_in=None, wall=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("bottle_adapter_neck_to_neck", {"d" : d, "neck_od1" : neck_od1, "neck_id1" : neck_id1, "thread_od1" : thread_od1, "height1" : height1, "support_od1" : support_od1, "thread_pitch1" : thread_pitch1, "neck_od2" : neck_od2, "neck_id2" : neck_id2, "thread_od2" : thread_od2, "height2" : height2, "support_od2" : support_od2, "pitch2" : pitch2, "taper_lead_in" : taper_lead_in, "wall" : wall, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sp_neck(_Bosl2Base):
    def __init__(self, diam=None, type=None, wall=None, id=None, style=None, bead=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sp_neck", {"diam" : diam, "type" : type, "wall" : wall, "id" : id, "style" : style, "bead" : bead, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sp_cap(_Bosl2Base):
    def __init__(self, diam=None, type=None, wall=None, style=None, top_adj=None, bot_adj=None, texture=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sp_cap", {"diam" : diam, "type" : type, "wall" : wall, "style" : style, "top_adj" : top_adj, "bot_adj" : bot_adj, "texture" : texture, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

