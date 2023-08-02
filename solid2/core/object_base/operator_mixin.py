
class OperatorMixin:
    def _union_op(self, x, unionType):
        """
        This makes u = a+b identical to:
        u = union()(a, b )
        """
        res = unionType()

        #add self or all its children to res
        if isinstance(self, unionType):
            for c in self._children:
                res.add(c)
        else:
            res.add(self)

        #add x or all its children to res
        if isinstance(x, unionType):
            for c in x._children:
                res.add(c)
        else:
            res.add(x)

        return res

    def _difference_op(self, x, differenceType):
        """
        This makes u = a - b identical to:
        u = difference()(a, b )
        """
        res = differenceType()

        if isinstance(self, differenceType) and len(self._children):
            for c in self._children:
                res.add(c)
        else:
            res.add(self)

        res.add(x)
        return res

    def _intersection_op(self, x, intersectionType):
        """
        This makes u = a * b identical to:
        u = intersection()(a, b )
        """
        res = intersectionType()

        if isinstance(self, intersectionType) and len(self._children):
            for c in self._children:
                res.add(c)
        else:
            res.add(self)

        if isinstance(x, intersectionType):
            for c in x._children:
                res.add(c)
        else:
            res.add(x)

        return res

    def __add__(self, x):
        from ..builtins import union
        return self._union_op(x, union)
    def __or__(self, x):
        from ..builtins import union
        return self._union_op(x, union)
    def __radd__(self, x):
        from ..builtins import union
        return union()(x)._union_op(self, union)
    def __sub__(self, x):
        from ..builtins import difference
        return self._difference_op(x, difference)
    def __mul__(self, x):
        from ..builtins import intersection
        return self._intersection_op(x, intersection)
    def __and__(self, x):
        from ..builtins import intersection
        return self._intersection_op(x, intersection)
    def __invert__(self):
        from .. import builtins; return builtins.debug()(self)

