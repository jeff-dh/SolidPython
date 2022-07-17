from solid.core.utils import indent
from solid.core.object_base import scad_inline, OpenSCADObject
from solid.extensions.greedy_scad_interface import ScadValue
import inspect

children = lambda i = "" : scad_inline(f"children({i});")

registeredModules = {}

def getRegisteredModulesStr():
    s = ""
    for f in registeredModules:
        s += registeredModules[f]

    return s

from solid.core.extension_manager import default_extension_manager
default_extension_manager.register_pre_render(lambda root : getRegisteredModulesStr())

def exportResultAsModule(func):
    def childrenToStr(args):
        s = ""
        for a in args:
            s += a._render()
            if s[-1] == "\n":
                s = s[:-1]
        return s

    def parametersToStr(args):
        s = ""
        for a in args:
            s += str(a) + ","
        if len(s):
            #cut of trailing ","
            s = s[:-1]
            if s[-1] == "\n":
                s = s[:-1]
            if s[-1] == ";":
                s = s[:-1]
        return s

    if not func in registeredModules:
        argSpecs = inspect.getfullargspec(func).args
        parameters = [ScadValue(p) for p in argSpecs]

        moduleCode = f"module {func.__name__}({parametersToStr(parameters)}){{\n"
        moduleCode += indent(func(*parameters)._render())
        moduleCode += "}\n"
        registeredModules[func] = moduleCode

    def wrapper(*args, **kwargs):
        argSpecs = inspect.getfullargspec(func).args
        params = dict(zip(argSpecs, args))
        params.update(kwargs)
        return OpenSCADObject(func.__name__, params)

    return wrapper

