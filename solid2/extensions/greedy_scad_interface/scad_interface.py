from solid2 import register_pre_render as _register_pre_render
from .scad_variable import ScadVariable as _ScadVariable,\
                           ScadValue as _ScadValue

_fonts = []

def register_font(filename):
    _fonts.append(filename)

def get_animation_time():
    return _ScadValue("$t")

def set_global_fn(_fn):
    _ScadVariable("$fn", _fn)

def set_global_fa(_fa):
    _ScadVariable("$fa", _fa)

def set_global_fs(_fs):
    _ScadVariable("$fs", _fs)

def set_global_viewport_translation(trans):
    _ScadVariable("$vpt", trans)

def set_global_viewport_rotation(rot):
    _ScadVariable("$vpr", rot)

def set_global_viewport_fov(fov):
    _ScadVariable("$vpf", fov)

def set_global_viewport_distance(d):
    _ScadVariable("$vpd", d)

def set_global_variable(var_name, value):
    _ScadVariable(var_name, value)

@_register_pre_render
def _get_scad_header(_):
    base_str = "\n".join([f"use <{f}>" for f in _fonts])
    base_str += "\n\n"
    base_str += "\n".join(_ScadVariable.registered_variables.values())

    return base_str + "\n"

