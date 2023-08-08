__nothing__ = None

from .bosl2_base import Bosl2Base as _Bosl2Base
from .std import union, attachable

#============ attachable add =============
#enhance the add function of the attachable OpenSCADObject so it can be used
#properly: cf. 07-libs-bosl2-attachable.py
attachable_default_add = attachable.add

def attachable_add(self, c):
    if len(self._children) == 0:
        attachable_default_add(self, c)
    elif len(self._children) == 1:
        attachable_default_add(self, union()(c))
    else:
        assert(len(self._children) == 2)
        self._children[1].add(c)

attachable.add = attachable_add
#============ attachable add end =============

# overwrite bosl2.shapes3d.cylinder to cover up a bug in
# solid2.core.builtins.cylinder
# unfortunately builtins.cylinder has a wrong (according to the docs) order of
# parameters and thus differs from the bosl2 implementation. To achieve
# consistency without creating major backwards compatibility issues, this hack
# is implemented to adjust the bosl2.cylinder according to the buggy
# builtins.cylinder.
class cylinder(_Bosl2Base):
    def __init__(self, r=None, h=None, r1=None, r2=None, d=None, d1=None,
                 d2=None, center=None, anchor=None, spin=None, orient=None,
                 **kwargs):
        super().__init__("cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" :
                                      center, "r" : r, "d" : d, "d1" : d1, "d2"
                                      : d2, "anchor" : anchor, "spin" : spin,
                                      "orient" : orient, **kwargs})

