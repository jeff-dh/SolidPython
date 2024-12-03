from solid2 import ScadValue as _ScadValue, \
                   scad_inline as _scad_inline, \
                   union as _union

from solid2.core.utils import indent as _indent

def scad_range(start, stop, step=1):
    return f"[{start}:{step}:{stop}]"

def scad_for(scadrange, loop_lambda):
    index = _ScadValue("scad_for_index")
    body = loop_lambda(index)._render()
    c = (f"for({index} = {scadrange}) {{\n"
         f"{_indent(body)}\n"
          "}\n")
    return _union()(_scad_inline(c))

def scad_if(condition, if_body, else_body):
    c = (f"if({condition}) {{\n"
         f"{_indent(if_body._render())}\n"
          "} else {\n"
         f"{_indent(else_body._render())}\n"
          "}\n")
    return _union()(_scad_inline(c))

