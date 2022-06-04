from ..core import builtins
from . import convenience
from ..core.utils import escape_openscad_identifier
from ..core.object_base import ObjectBase
from ..config import config

__nothing__ = None

# ===============================
# = monkey patch ObjectBase =
# ===============================
"""
    Patch ObjectBase to allow .-access syntax style:

    cube(20).translate(1, 2, 3) + cylinder(r=0.5, h=5).up(5).rotate(20, 30, 40)
"""

#builtin transformations
_cascading_builtins = ("union difference intersection translate " +\
                      "scale rotate linear_extrude rotate_extrude").split(" ")
if not config.use_implicit_builtins:
    _cascading_builtins += ("intersection_for mirror resize color offset hull render " +\
                            "projection surface").split(" ")

def add_builtin_to_object_base(name):
    #get the builtin
    builtin = getattr(builtins, escape_openscad_identifier(name))

    func = lambda self, *args, **kwargs : builtin(*args, **kwargs)(self)

    setattr(ObjectBase, escape_openscad_identifier(name), func)

for name in _cascading_builtins:
    add_builtin_to_object_base(name)

#replace basic transformations with wrappers from the convenience module
ObjectBase.translate = lambda self, *args, **kwargs: convenience.translate(*args, **kwargs)(self)
ObjectBase.mirror = lambda self, *args, **kwargs: convenience.mirror(*args, **kwargs)(self)
ObjectBase.scale = lambda self, *args, **kwargs: convenience.scale(*args, **kwargs)(self)
ObjectBase.resize = lambda self, *args, **kwargs: convenience.resize(*args, **kwargs)(self)
ObjectBase.rotate = lambda self, *args, **kwargs: convenience.rotate(*args, **kwargs)(self)
ObjectBase.offset = lambda self, *args, **kwargs: builtins.offset(*args, **kwargs)(self)

#translation, mirror, scale, rotate and resize convenience wrappers
ObjectBase.down = lambda self, x: convenience.down(x)(self)
ObjectBase.up = lambda self, x: convenience.up(x)(self)
ObjectBase.left = lambda self, x: convenience.left(x)(self)
ObjectBase.right = lambda self, x: convenience.right(x)(self)
ObjectBase.back = lambda self, x: convenience.back(x)(self)
ObjectBase.fwd = lambda self, x: convenience.fwd(x)(self)
ObjectBase.forward = lambda self, x: convenience.fwd(x)(self)
ObjectBase.mirrorX = lambda self: convenience.mirrorX()(self)
ObjectBase.mirrorY = lambda self: convenience.mirrorY()(self)
ObjectBase.mirrorZ = lambda self: convenience.mirrorZ()(self)
ObjectBase.scaleX = lambda self, x: convenience.scaleX(x)(self)
ObjectBase.scaleY = lambda self, y: convenience.scaleY(y)(self)
ObjectBase.scaleZ = lambda self, z: convenience.scaleZ(z)(self)
ObjectBase.rotateX = lambda self, x: convenience.rotateX(x)(self)
ObjectBase.rotateY = lambda self, y: convenience.rotateY(y)(self)
ObjectBase.rotateZ = lambda self, z: convenience.rotateZ(z)(self)
ObjectBase.resizeX = lambda self, x: convenience.resizeX(x)(self)
ObjectBase.resizeY = lambda self, y: convenience.resizeY(y)(self)
ObjectBase.resizeZ = lambda self, z: convenience.resizeZ(z)(self)
ObjectBase.translateX = lambda self, x: convenience.translateX(x)(self)
ObjectBase.translateY = lambda self, y: convenience.translateY(y)(self)
ObjectBase.translateZ = lambda self, z: convenience.translateZ(z)(self)

#debug, background, root, disable and ~
ObjectBase.debug = lambda self: builtins.debug()(self)
ObjectBase.background = lambda self: builtins.background()(self)
ObjectBase.root = lambda self: builtins.root()(self)
ObjectBase.disable = lambda self: builtins.disable()(self)

