#! /usr/bin/env python

from pathlib import Path

from solid2.core.utils import escape_openscad_identifier as escape
from solid2.libs.py_scadparser import scad_parser

from openscad_extension_generator import generateStub, makePackage

headerTemplate = """\
from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{{_Path(__file__).parent.parent / '{scadFile}'}}", {use_not_include})

"""

callableTemplate = """\
class {name}(_Bosl2Base):
    def __init__({paramStr}):
       super().__init__({initStr})

"""

mixinHeader = """
from solid2.core.object_base import AccessSyntaxMixin as _AccessSyntaxMixin

class Bosl2AccessSyntaxMixin(_AccessSyntaxMixin):

    def _get_std(self):
        from . import std
        return std
"""
mixinTemplate = """
    def {name}(self, {paramListWithDefaults}**kwargs):
        return self._get_std().{name}({paramList}**kwargs)(self)
"""

scad_builtins_primitives = \
    Path(__file__).parent.parent / "core" / "builtins" / "openscad.primitives"

def generateBosl2Std(bosl2_dir):
    stubFile = Path(__file__).absolute().parent / "bosl2" / "std.py"

    with open(stubFile, "w") as std_f:
        std_f.write("from .openscad import *\n")
        with open(bosl2_dir / "std.scad") as f:
            for l in f.readlines():
                l = l.strip()
                if not l.startswith("include <"):
                    continue
                l = l.replace("include <", "").replace(">", "")
                if Path(l).stem not in ["math", "lists", "strings", "utility"]:
                    std_f.write(f"from .{Path(l).stem} import *\n")
                else:
                    std_f.write(f"from . import {Path(l).stem} as bosl2_{Path(l).stem}\n")

def generateBosl2AccessSyntaxMixin(bosl2_dir, outputDir):
    def generateCallable(c):
        name = escape(c.name)
        paramNames = [escape(p.name) for p in c.parameters]
        paramNames = list(dict.fromkeys(paramNames))

        paramListWithDefaults = ", ".join([f"{p}=None" for p in paramNames])
        paramList = ", ".join([f'{p}' for p in paramNames])

        if paramListWithDefaults: paramListWithDefaults += ", "
        if paramList: paramList += ", "

        return mixinTemplate.format(name=name,
                                    paramListWithDefaults=paramListWithDefaults,
                                    paramList=paramList)

    mods = ["transforms", "attachments", "miscellaneous",
            "distributors", "partitions", "color"]

    mixinFiles = [(bosl2_dir / m).with_suffix(".scad") for m in mods]

    modules = []
    for f in mixinFiles:
        m, _, _ = scad_parser.parseFile(f)
        modules += m


    with open(outputDir / "bosl2_access_syntax_mixin.py", "w") as f:
        f.write(mixinHeader)

        for c in modules:
            if c.name.startswith("_"):
                continue
            f.write(generateCallable(c))

bosl2_dir = Path("./bosl2/BOSL2")
output_dir = Path(__file__).parent / "bosl2"

makePackage(output_dir)
generateBosl2Std(bosl2_dir)
generateBosl2AccessSyntaxMixin(bosl2_dir, output_dir)

for f in bosl2_dir.iterdir():
    if not f.suffix == ".scad":
        continue
    if f.name in ["std.scad", "builtins.scad", "bosl1compat.scad"]:
        continue

    generateStub(f, output_dir, False,
                 headerTemplate=headerTemplate,
                 callableTemplate=callableTemplate)

generateStub(scad_builtins_primitives, output_dir, False,
             headerTemplate=\
                 "from .bosl2_base import Bosl2Base as _Bosl2Base\n\n",
             callableTemplate=callableTemplate)

