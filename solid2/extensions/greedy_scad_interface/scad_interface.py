from solid2 import register_pre_render as _register_pre_render
from .scad_variable import *

fonts = []

def register_font(filename):
    fonts.append(filename)

def get_animation_time():
    return ScadValue("$t")

def set_global_fn(_fn):
    ScadVariable("$fn", _fn)

def set_global_fa(_fa):
    ScadVariable("$fa", _fa)

def set_global_fs(_fs):
    ScadVariable("$fs", _fs)

def set_global_viewport_translation(trans):
    ScadVariable("$vpt", trans)

def set_global_viewport_rotation(rot):
    ScadVariable("$vpr", rot)

def set_global_viewport_fov(fov):
    ScadVariable("$vpf", fov)

def set_global_viewport_distance(d):
    ScadVariable("$vpd", d)

def set_global_variable(var_name, value):
    ScadVariable(var_name, value)

@_register_pre_render
def _get_scad_header(_):
    base_str = "\n".join([f"use <{f}>" for f in fonts])
    base_str += "\n\n"
    base_str += "\n".join(ScadVariable.registered_variables.values())

    return base_str + "\n"

