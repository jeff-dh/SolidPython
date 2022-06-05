from solid.core.utils import indent
from solid.core.object_base import ObjectBase, scad_inline
import inspect

registeredModules = {}

def getRegisteredModulesStr():
    s = ""
    for f in registeredModules:
        s += registeredModules[f]

    return s

from solid.core.extension_manager import default_extension_manager
default_extension_manager.register_pre_render(lambda root : getRegisteredModulesStr())

def exportReturnValueAsModule(func):
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
        parameters = [scad_inline(p) for p in argSpecs if not p == 'children']

        childrenFunc = lambda i : scad_inline(f"children({i});\n")

        moduleCode = f"module {func.__name__}({parametersToStr(parameters)}){{\n"
        moduleCode += indent(func(*parameters, children=childrenFunc)._render())
        moduleCode += "}\n"
        registeredModules[func] = moduleCode

    def wrapper(*args):
        parameters = [a for a in args if not issubclass(a.__class__, ObjectBase)]
        children = [a for a in args if issubclass(a.__class__, ObjectBase)]

        childrenStr = f"{{{childrenToStr(children)}}}" if len(children) else ""
        parameterStr = parametersToStr(parameters)
        return scad_inline(f"{func.__name__}({parameterStr})" + childrenStr + ";\n")

    return wrapper

