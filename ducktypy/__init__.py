# coding: utf-8

from __future__ import absolute_import, unicode_literals


__all__ = ['Duck']


def _noinit(self, *args, **kwargs):
    raise RuntimeError(
        '"{}" is not for instantiation.'
        .format(type(self))
    )


_REGISTRY = {}


class Duck(type):

    REGISTRY = {}
    base_type = (object,)

    def __instancecheck__(cls, other):
        for attr in cls._requirements:
            if not hasattr(other, attr):
                return False
        return isinstance(other, cls._base_type)

    def __subclasscheck__(cls, othercls):
        for attr in cls._requirements:
            if not hasattr(othercls, attr):
                return False
        return issubclass(othercls, cls._base_type)

    @classmethod
    def based(cls, *types):
        if not types:
            types = object,
        try:
            return _REGISTRY[types]
        except KeyError:
            subduck = type(
                str('_'.join(t.__name__ for t in types) + '_Duck'),
                (Duck, ),
                {str('base_type'): types,}
            )
            _REGISTRY[types] = subduck
            return subduck

    @classmethod
    def has(meta, *attrs):
        attrs = frozenset(str(a) for a in attrs)
        try:
            return meta.REGISTRY[attrs]
        except KeyError:
            attributes = {name: False for name in attrs}
            attributes.update(
                __init__=_noinit,
                _requirements=attrs,
                _base_type=meta.base_type,
            )
            duck = Duck(
                str(meta.__name__ + '_has__' + '__'.join(attrs)),
                meta.base_type,
                attributes,
            )
            meta.REGISTRY[attrs] = duck
            return duck

_REGISTRY[object,] = Duck
