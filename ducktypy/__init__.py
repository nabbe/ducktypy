# coding: utf-8

from __future__ import absolute_import, unicode_literals


def noinit(self, *args, **kwargs):
    raise RuntimeError(
        '"{}" is not for instantiation.'
        .format(type(self))
    )


class Duck(type):

    REGISTRY = {}

    def __instancecheck__(cls, other):
        for attr in cls._requirements:
            if not hasattr(other, attr):
                return False
        return True

    def __subclasscheck__(cls, othercls):
        for attr in cls._requirements:
            if not hasattr(othercls, attr):
                return False
        return True

    @classmethod
    def has(meta, *attrs):
        attrs = tuple(sorted(attrs))
        try:
            return meta.REGISTRY[attrs]
        except KeyError:
            duck = Duck(
                str('Duck_has__' + '__'.join(attrs)),
                (object,),
                {
                    str('__init__'): noinit,
                    str('_requirements'): attrs,
                }
            )
            meta.REGISTRY[attrs] = duck
            return duck
