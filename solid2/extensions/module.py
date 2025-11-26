import hashlib

from solid2 import register_pre_render as _register_pre_render
from solid2.core.object_base import ObjectBase as _ObjectBase
from solid2.core.object_base.access_syntax_mixin import (
    AccessSyntaxMixin as _AccessSyntaxMixin,
)
from solid2.core.object_base.operator_mixin import OperatorMixin as _OperatorMixin
from solid2.core.utils import indent as _indent

# Global registry of all modules that need to be rendered
_module_registry = {}


def _reset_module_registry():
    """Reset the module registry. Useful for testing."""
    global _module_registry
    _module_registry = {}


def _get_module_definitions():
    """Get all module definitions that need to be rendered."""
    return _module_registry


class Module(_ObjectBase):
    """
    Wraps an OpenSCAD object tree as a module for performance optimization.
    Modules are cached by OpenSCAD, which improves rendering performance
    for complex shapes that are used multiple times.
    """

    def __init__(self, obj, name=None, name_prefix="mod"):
        super().__init__()
        self._obj = obj

        # Generate or use provided name
        if name:
            self._module_name = name
        else:
            # Generate stable name based on content hash
            content = obj._render()
            content_hash = hashlib.sha256(content.encode()).hexdigest()[:8]
            self._module_name = f"{name_prefix}_{content_hash}"

        # Register this module globally, checking for duplicates
        # Only error if user explicitly provided a name (not auto-generated)
        if name is not None and self._module_name in _module_registry:
            raise ValueError(
                f"Module name '{self._module_name}' already exists. "
                f"Please choose a different name."
            )

        # Register the module (auto-generated names can reuse existing registration)
        if self._module_name not in _module_registry:
            _module_registry[self._module_name] = self._obj

    def _render(self):
        """
        Render module instantiation (just the call).
        The module definition itself is rendered separately.
        """
        return f"{self._module_name}();\n"

    def __call__(self, *args):
        """
        Create a new instance of this module.
        If called with no arguments, returns self.
        If called with arguments, adds them as children (standard OpenSCAD behavior).
        """
        if not args:
            # Return a new instance that can be transformed
            return ModuleInstance(self._module_name)
        else:
            # Add children if provided
            return super().__call__(*args)


class ModuleInstance(_AccessSyntaxMixin, _OperatorMixin, _ObjectBase):
    """
    Represents an instantiation of a module.
    This allows the module to be transformed without affecting the original.
    """

    def __init__(self, module_name):
        super().__init__()
        self._module_name = module_name

    def _render(self):
        """Render module instantiation with any children/transformations."""

        if self._children:
            # If there are children, render them inside
            rendered_children = [_indent(child._render()) for child in self._children]
            return f"{self._module_name}() {{\n{''.join(rendered_children)}}}\n"
        else:
            # Simple instantiation
            return f"{self._module_name}();\n"


def module(obj, name=None, name_prefix="mod"):
    """
    Create a reusable OpenSCAD module from an object tree.

    Modules are cached by OpenSCAD and provide performance benefits when
    complex shapes are used multiple times.

    Args:
        obj: The OpenSCAD object tree to wrap in a module
        name: Optional custom name for the module. If not provided,
              a stable name will be generated based on the content hash.
              Explicit names must be unique, but auto-generated names can
              be reused (same content = same module).
        name_prefix: Prefix to use for auto-generated names. Defaults to "mod".
                     Only used when name is not provided.

    Returns:
        A Module object that can be instantiated multiple times

    Raises:
        ValueError: If an explicit name is provided that already exists

    Example:
        >>> my_shape = module(cube(5) + sphere(3), name="my_shape")
        >>> scene = my_shape() + my_shape().translate([10, 0, 0])
        >>>
        >>> # With custom prefix
        >>> gear = module(cylinder(r=5, h=2), name_prefix="gear")
        >>> # Generates name like "gear_a3f2c1b8"
        >>>
        >>> # Explicit duplicate names raise an error
        >>> mod1 = module(cube(5), name="shape")
        >>> mod2 = module(sphere(3), name="shape")  # ValueError!
        >>>
        >>> # Auto-generated names can be reused (same content)
        >>> mod3 = module(cube(5))  # auto-generated name
        >>> mod4 = module(cube(5))  # OK! Reuses same module registration
    """
    return Module(obj, name=name, name_prefix=name_prefix)


def render_module_definitions():
    """
    Render all module definitions.
    This should be called during the pre_render phase.
    """
    if not _module_registry:
        return ""

    output = []
    for module_name, obj in _module_registry.items():
        # Render the module definition
        obj_render = obj._render()
        # Indent the content
        indented_content = _indent(obj_render)
        output.append(f"module {module_name}() {{\n{indented_content}}}\n")

    return "\n".join(output) + "\n"


def _module_pre_render_hook(_root):
    """Hook function for pre_render phase to output module definitions."""
    return render_module_definitions()


_register_pre_render(_module_pre_render_hook)
