from ...config import config

def builtins():
    from .. import builtins
    return builtins

class AccessSyntaxMixin:
    if not config.use_implicit_builtins:
        def intersection_for(self, n):     return builtins().intersection_for(n)(self)
        def color(self, color, alpha=1.0): return builtins().color(color, alpha)(self)
        def hull(self):                    return builtins().hull()(self)
        def render(self, convexity=None):  return builtins().render(convexity)(self)
        def projection(self, cut=None):    return builtins().projection(cut)(self)

        def surface(self, file, center=None, convexity=None, invert=None):
            return builtins().surface(file, center, convexity, invert)(self)
        def offset(self, r=None, delta=None, chamfer=None, _fn=None):
            return builtins().offset(r, delta, chamfer, _fn)(self)

        def mirror(self, *args, **kwargs): return builtins().mirror(*args, **kwargs)(self)
        def resize(self, *args, **kwargs): return builtins().resize(*args, **kwargs)(self)

        def mirrorX(self): return builtins().mirrorX()(self)
        def mirrorY(self): return builtins().mirrorY()(self)
        def mirrorZ(self): return builtins().mirrorZ()(self)

        def resizeX(self, x): return builtins().resizeX(x)(self)
        def resizeY(self, y): return builtins().resizeY(y)(self)
        def resizeZ(self, z): return builtins().resizeZ(z)(self)

    def union(self):          return builtins().union()(self)
    def difference(self):     return builtins().difference()(self)
    def intersection(self):   return builtins().intersection()(self)


    def rotate_extrude(self, angle=None, convexity=None, _fn=None):
        return builtins().rotate_extrude(angle, convexity, _fn)(self)

    def linear_extrude(self, height=None, center=None, convexity=None, \
                       twist=None, slices=None, scale=None):
        return builtins().linear_extrude(height, center, convexity, twist,
                                         slices, scale)(self)

    def translate(self, *args, **kwargs): return builtins().translate(*args, **kwargs)(self)
    def scale(self, *args, **kwargs):     return builtins().scale(*args, **kwargs)(self)
    def rotate(self, *args, **kwargs):    return builtins().rotate(*args, **kwargs)(self)

    def down(self, z):    return builtins().down(z)(self)
    def up(self, z):      return builtins().up(z)(self)
    def left(self, x):    return builtins().left(x)(self)
    def right(self, x):   return builtins().right(x)(self)
    def back(self, y):    return builtins().back(y)(self)
    def fwd(self, y):     return builtins().fwd(y)(self)
    def forward(self, y): return builtins().fwd(y)(self)

    def translateX(self, x): return builtins().translateX(x)(self)
    def translateY(self, y): return builtins().translateY(y)(self)
    def translateZ(self, z): return builtins().translateZ(z)(self)

    def rotateX(self, x): return builtins().rotateX(x)(self)
    def rotateY(self, y): return builtins().rotateY(y)(self)
    def rotateZ(self, z): return builtins().rotateZ(z)(self)

    def scaleX(self, x): return builtins().scaleX(x)(self)
    def scaleY(self, y): return builtins().scaleY(y)(self)
    def scaleZ(self, z): return builtins().scaleZ(z)(self)

    def debug(self):      return builtins().debug()(self)
    def background(self): return builtins().background()(self)
    def root(self):       return builtins().root()(self)
    def disable(self):    return builtins().disable()(self)

    def __getattr__(self, name):
        #ask the extension manager for dynamic access syntax extensions
        from ..extension_manager import default_extension_manager

        fn = default_extension_manager.access_syntax_lookup(name)
        if not fn:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

        return lambda *args, **kwargs: fn(self, *args, **kwargs)
