from .access_syntax_mixin import AccessSyntaxMixin
from .operator_mixin import OperatorMixin

#don't do relative imports on the global scope to be able to import this file
#from "everywhere"

class RenderMixin:
    def __repr__(self):
        return self.as_scad()

    def as_scad(self):
        from ..scad_render import scad_render
        return scad_render(self)[:-1]

    def save_as_scad(self, filename='', outdir=''):
        from ..scad_render import scad_render_to_file
        return scad_render_to_file(self, filename, outdir)

    def save_as_stl(self, filename=None):
        from ..scad_render import render_to_stl_file
        return render_to_stl_file(self, filename)

    def _ipython_display_(self):
        from IPython import get_ipython, display

        def is_notebook():
            return get_ipython().__class__.__name__ == 'ZMQInteractiveShell'

        if is_notebook():
            try:
                from jupyterscad import render
            except ImportError:
                print(self.as_scad())
                return

            display.display(render(self))

class ObjectBase(RenderMixin):
    def __init__(self):
        self._children = []

    def add(self, c):
        def _add(c):
            assert(hasattr(c, "_render"))
            self._children += [c]

        if isinstance(c, list):
            for cc in c:
                _add(cc)
        else:
            _add(c)

        return self

    def _render(self):
        s = ''
        for c in self._children:
            s += c._render()
        return s

    def __call__(self, *args):
        #translate(...)(cube())
        #this adds cube() to translate._children
        for a in args:
            self.add(a)
        return self


class BareOpenSCADObject(ObjectBase):
    def __init__(self, name, params):
        super().__init__()
        self._name = name
        self._params = params

    def _render(self):
        """
            returns the scad code for a given node tuple consiting of name,
            params and children list.

            -> translate(v = [1, 2, 3]) {children[0]; children[1]; ...};\n
        """
        from ..utils import indent
        renderedChildsList = [indent(child._render()) for child in self._children]
        if renderedChildsList:
            renderedChilds = f" {{\n{''.join(renderedChildsList)}}}\n"
        else:
            renderedChilds = ";\n"

        return self._generate_scad_head() + renderedChilds

    def _generate_scad_head(self):
        """
            for a given function name and dict of params it returns:
                {name}(p1=v1, p2=v2,...)
                -> translate(v = [1, 2, 3])
        """
        from ..utils import unescape_openscad_identifier, py2openscad
        from ...config import config

        param_strings = []
        for p in sorted(self._params.keys()):
            if self._params[p] is None:
                continue

            if config.use_implicit_builtins and \
                        isinstance(self._params[p], OpenSCADParameterFunction):

                param_strings.append(self._params[p]._render())
            else:
                scad_value = py2openscad(self._params[p])
                scad_identifier = unescape_openscad_identifier(p)

                param_strings.append(f'{scad_identifier} = {scad_value}')

        scad_identifier = unescape_openscad_identifier(self._name)
        param_str = ", ".join(param_strings)

        return f'{scad_identifier}({param_str})'

class OpenSCADObject(AccessSyntaxMixin, OperatorMixin, BareOpenSCADObject):
    pass

class OpenSCADConstant:
    def __init__(self, value):
        self.value = value

        from ..utils import escape_openscad_identifier
        self.__doc__ = escape_openscad_identifier(value)

    def __repr__(self):
        return f'{self.value}'

    def __operator_base__(self, op, other):
        return OpenSCADConstant(f'({self} {op} {other})')

    def __roperator_base__(self, op, other):
        return OpenSCADConstant(f'({other} {op} {self})')

    def __unary_operator_base__(self, op):
        return OpenSCADConstant(f'({op}{self})')

    def __illegal_operator__(self):
       raise Exception("You can't compare a OpenSCADConstant with something else, " +\
                       "because we don't know the customized value at " +\
                       "SolidPythons runtime because it might get customized " +\
                       "at OpenSCAD runtime.")

    #basic operators +, -, *, /, %, **
    def __add__(self, other): return self.__operator_base__("+", other)
    def __sub__(self, other): return self.__operator_base__("-", other)
    def __mul__(self, other): return self.__operator_base__("*", other)
    def __mod__(self, other): return self.__operator_base__("%", other)
    def __pow__(self, other): return self.__operator_base__("^", other)
    def __truediv__(self, other): return self.__operator_base__("/", other)

    def __radd__(self, other): return self.__roperator_base__("+", other)
    def __rsub__(self, other): return self.__roperator_base__("-", other)
    def __rmul__(self, other): return self.__roperator_base__("*", other)
    def __rmod__(self, other): return self.__roperator_base__("%", other)
    def __rpow__(self, other): return self.__roperator_base__("^", other)
    def __rtruediv__(self, other): return self.__roperator_base__("/", other)

    #unary operators
    def __neg__(self): return self.__unary_operator_base__("-")

    #other operators
    def __abs__(self): return OpenSCADConstant(f'abs({self})')

    #"illegal" operators
    def __eq__(self, other): return self.__operator_base__("==", other) #type: ignore
    def __ne__(self, other): return self.__operator_base__("!=", other) #type: ignore
    def __le__(self, other): return self.__operator_base__("<=", other)
    def __ge__(self, other): return self.__operator_base__(">=", other)
    def __lt__(self, other): return self.__operator_base__("<", other)
    def __gt__(self, other): return self.__operator_base__(">", other)

    #do not allow to evaluate to bool
    def __bool__(self):
        raise Exception("You can't evaluate scad variables because " +\
                        "we don't know the value of the variable at " +\
                        "SolidPython runtime.")

    def _render(self):
        from textwrap import dedent
        return dedent(self.value)

def scad_inline(code):
    return OpenSCADConstant(code)

class OpenSCADParameterFunction(OpenSCADConstant):
    pass

def scad_inline_parameter_func(code):
    return OpenSCADParameterFunction(code)

