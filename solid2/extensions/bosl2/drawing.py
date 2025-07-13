from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/drawing.scad'}", False)

class stroke(_Bosl2Base):
    def __init__(self, path=None, width=None, closed=None, endcaps=None, endcap1=None, endcap2=None, joints=None, dots=None, endcap_width=None, endcap_width1=None, endcap_width2=None, joint_width=None, dots_width=None, endcap_length=None, endcap_length1=None, endcap_length2=None, joint_length=None, dots_length=None, endcap_extent=None, endcap_extent1=None, endcap_extent2=None, joint_extent=None, dots_extent=None, endcap_angle=None, endcap_angle1=None, endcap_angle2=None, joint_angle=None, dots_angle=None, endcap_color=None, endcap_color1=None, endcap_color2=None, joint_color=None, dots_color=None, color=None, trim=None, trim1=None, trim2=None, singleton_scale=None, convexity=None, **kwargs):
       super().__init__("stroke", {"path" : path, "width" : width, "closed" : closed, "endcaps" : endcaps, "endcap1" : endcap1, "endcap2" : endcap2, "joints" : joints, "dots" : dots, "endcap_width" : endcap_width, "endcap_width1" : endcap_width1, "endcap_width2" : endcap_width2, "joint_width" : joint_width, "dots_width" : dots_width, "endcap_length" : endcap_length, "endcap_length1" : endcap_length1, "endcap_length2" : endcap_length2, "joint_length" : joint_length, "dots_length" : dots_length, "endcap_extent" : endcap_extent, "endcap_extent1" : endcap_extent1, "endcap_extent2" : endcap_extent2, "joint_extent" : joint_extent, "dots_extent" : dots_extent, "endcap_angle" : endcap_angle, "endcap_angle1" : endcap_angle1, "endcap_angle2" : endcap_angle2, "joint_angle" : joint_angle, "dots_angle" : dots_angle, "endcap_color" : endcap_color, "endcap_color1" : endcap_color1, "endcap_color2" : endcap_color2, "joint_color" : joint_color, "dots_color" : dots_color, "color" : color, "trim" : trim, "trim1" : trim1, "trim2" : trim2, "singleton_scale" : singleton_scale, "convexity" : convexity, **kwargs})

class dashed_stroke(_Bosl2Base):
    def __init__(self, path=None, dashpat=None, closed=None, fit=None, mindash=None, **kwargs):
       super().__init__("dashed_stroke", {"path" : path, "dashpat" : dashpat, "closed" : closed, "fit" : fit, "mindash" : mindash, **kwargs})

class arc(_Bosl2Base):
    def __init__(self, n=None, r=None, angle=None, d=None, cp=None, points=None, corner=None, width=None, thickness=None, start=None, wedge=None, long=None, cw=None, ccw=None, endpoint=None, rounding=None, **kwargs):
       super().__init__("arc", {"n" : n, "r" : r, "angle" : angle, "d" : d, "cp" : cp, "points" : points, "corner" : corner, "width" : width, "thickness" : thickness, "start" : start, "wedge" : wedge, "long" : long, "cw" : cw, "ccw" : ccw, "endpoint" : endpoint, "rounding" : rounding, **kwargs})

class _rounded_arc(_Bosl2Base):
    def __init__(self, radius=None, rounding=None, angle=None, n=None, **kwargs):
       super().__init__("_rounded_arc", {"radius" : radius, "rounding" : rounding, "angle" : angle, "n" : n, **kwargs})

class catenary(_Bosl2Base):
    def __init__(self, width=None, droop=None, n=None, angle=None, **kwargs):
       super().__init__("catenary", {"width" : width, "droop" : droop, "n" : n, "angle" : angle, **kwargs})

class helix(_Bosl2Base):
    def __init__(self, l=None, h=None, turns=None, angle=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, **kwargs):
       super().__init__("helix", {"l" : l, "h" : h, "turns" : turns, "angle" : angle, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, **kwargs})

class _normal_segment(_Bosl2Base):
    def __init__(self, p1=None, p2=None, **kwargs):
       super().__init__("_normal_segment", {"p1" : p1, "p2" : p2, **kwargs})

class turtle(_Bosl2Base):
    def __init__(self, commands=None, state=None, full_state=None, repeat=None, **kwargs):
       super().__init__("turtle", {"commands" : commands, "state" : state, "full_state" : full_state, "repeat" : repeat, **kwargs})

class _turtle_repeat(_Bosl2Base):
    def __init__(self, commands=None, state=None, full_state=None, repeat=None, **kwargs):
       super().__init__("_turtle_repeat", {"commands" : commands, "state" : state, "full_state" : full_state, "repeat" : repeat, **kwargs})

class _turtle_command_len(_Bosl2Base):
    def __init__(self, commands=None, index=None, **kwargs):
       super().__init__("_turtle_command_len", {"commands" : commands, "index" : index, **kwargs})

class _turtle(_Bosl2Base):
    def __init__(self, commands=None, state=None, full_state=None, index=None, **kwargs):
       super().__init__("_turtle", {"commands" : commands, "state" : state, "full_state" : full_state, "index" : index, **kwargs})

class _turtle_command(_Bosl2Base):
    def __init__(self, command=None, parm=None, parm2=None, state=None, index=None, **kwargs):
       super().__init__("_turtle_command", {"command" : command, "parm" : parm, "parm2" : parm2, "state" : state, "index" : index, **kwargs})

class stroke(_Bosl2Base):
    def __init__(self, path=None, width=None, closed=None, endcaps=None, endcap1=None, endcap2=None, joints=None, dots=None, endcap_width=None, endcap_width1=None, endcap_width2=None, joint_width=None, dots_width=None, endcap_length=None, endcap_length1=None, endcap_length2=None, joint_length=None, dots_length=None, endcap_extent=None, endcap_extent1=None, endcap_extent2=None, joint_extent=None, dots_extent=None, endcap_angle=None, endcap_angle1=None, endcap_angle2=None, joint_angle=None, dots_angle=None, endcap_color=None, endcap_color1=None, endcap_color2=None, joint_color=None, dots_color=None, color=None, trim=None, trim1=None, trim2=None, singleton_scale=None, convexity=None, **kwargs):
       super().__init__("stroke", {"path" : path, "width" : width, "closed" : closed, "endcaps" : endcaps, "endcap1" : endcap1, "endcap2" : endcap2, "joints" : joints, "dots" : dots, "endcap_width" : endcap_width, "endcap_width1" : endcap_width1, "endcap_width2" : endcap_width2, "joint_width" : joint_width, "dots_width" : dots_width, "endcap_length" : endcap_length, "endcap_length1" : endcap_length1, "endcap_length2" : endcap_length2, "joint_length" : joint_length, "dots_length" : dots_length, "endcap_extent" : endcap_extent, "endcap_extent1" : endcap_extent1, "endcap_extent2" : endcap_extent2, "joint_extent" : joint_extent, "dots_extent" : dots_extent, "endcap_angle" : endcap_angle, "endcap_angle1" : endcap_angle1, "endcap_angle2" : endcap_angle2, "joint_angle" : joint_angle, "dots_angle" : dots_angle, "endcap_color" : endcap_color, "endcap_color1" : endcap_color1, "endcap_color2" : endcap_color2, "joint_color" : joint_color, "dots_color" : dots_color, "color" : color, "trim" : trim, "trim1" : trim1, "trim2" : trim2, "singleton_scale" : singleton_scale, "convexity" : convexity, **kwargs})

class dashed_stroke(_Bosl2Base):
    def __init__(self, path=None, dashpat=None, width=None, closed=None, fit=None, roundcaps=None, **kwargs):
       super().__init__("dashed_stroke", {"path" : path, "dashpat" : dashpat, "width" : width, "closed" : closed, "fit" : fit, "roundcaps" : roundcaps, **kwargs})

class arc(_Bosl2Base):
    def __init__(self, n=None, r=None, angle=None, d=None, cp=None, points=None, corner=None, width=None, thickness=None, start=None, wedge=None, rounding=None, anchor=None, spin=None, **kwargs):
       super().__init__("arc", {"n" : n, "r" : r, "angle" : angle, "d" : d, "cp" : cp, "points" : points, "corner" : corner, "width" : width, "thickness" : thickness, "start" : start, "wedge" : wedge, "rounding" : rounding, "anchor" : anchor, "spin" : spin, **kwargs})

class catenary(_Bosl2Base):
    def __init__(self, width=None, droop=None, n=None, angle=None, anchor=None, spin=None, **kwargs):
       super().__init__("catenary", {"width" : width, "droop" : droop, "n" : n, "angle" : angle, "anchor" : anchor, "spin" : spin, **kwargs})

class helix(_Bosl2Base):
    def __init__(self, l=None, h=None, turns=None, angle=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, **kwargs):
       super().__init__("helix", {"l" : l, "h" : h, "turns" : turns, "angle" : angle, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, **kwargs})

class turtle(_Bosl2Base):
    def __init__(self, commands=None, state=None, full_state=None, repeat=None, **kwargs):
       super().__init__("turtle", {"commands" : commands, "state" : state, "full_state" : full_state, "repeat" : repeat, **kwargs})

class debug_polygon(_Bosl2Base):
    def __init__(self, points=None, paths=None, vertices=None, edges=None, convexity=None, size=None, **kwargs):
       super().__init__("debug_polygon", {"points" : points, "paths" : paths, "vertices" : vertices, "edges" : edges, "convexity" : convexity, "size" : size, **kwargs})

class _debug_poly_verts(_Bosl2Base):
    def __init__(self, points=None, size=None, **kwargs):
       super().__init__("_debug_poly_verts", {"points" : points, "size" : size, **kwargs})

class _debug_poly_edges(_Bosl2Base):
    def __init__(self, j=None, points=None, path=None, vertices=None, size=None, **kwargs):
       super().__init__("_debug_poly_edges", {"j" : j, "points" : points, "path" : path, "vertices" : vertices, "size" : size, **kwargs})

