from solid.extensions.greedy_scad_interface import *
from solid.core.utils import indent
import inspect

registeredModules = {}

def getCompileFunctionsHeader():
    s = ""
    for f in registeredModules:
        s += registeredModules[f]

    return s

from solid.core.extension_manager import default_extension_manager
default_extension_manager.register_pre_render(lambda root : getCompileFunctionsHeader())

def exportReturnValueAsModule(func):
    def parametersToStr(args):
        s = ""
        for a in args:
            s += str(a) + ","
        if len(s):
            #cut of trailing ","
            s = s[:-1]
        return s

    if not func in registeredModules:
        argSpecs = inspect.getfullargspec(func).args 
        parameters = [ScadValue(p) for p in argSpecs]

        moduleCode = f"module {func.__name__}({parametersToStr(argSpecs)}){{\n"
        moduleCode += indent(func(*parameters)._render())
        moduleCode += "}\n"
        registeredModules[func] = moduleCode

    return lambda *args : ScadValue(f"{func.__name__}({parametersToStr(args)});")

