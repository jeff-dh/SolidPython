__nothing__ = None

from .bosl2_base import Bosl2Base
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

# flip back & fwd -> issue #54
# https://github.com/jeff-dh/SolidPython/issues/54
back = Bosl2Base.back
Bosl2Base.back = Bosl2Base.fwd #type: ignore
Bosl2Base.fwd = back #type: ignore
