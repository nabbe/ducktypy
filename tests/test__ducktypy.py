# coding: utf-8

from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from ducktypy import Duck


class Bird(object):
    wing = 'fluffy'

class Albatross(Bird):
    def fly(self):
        return 'quietly'

class Ostrich(Bird):
    def run(self):
        return 'super fast!'

class Airplain(object):
    wing = 'Duralmin'
    def fly(self):
        return 'jet-engine powered!'


class ExampleException(Exception):
    pass

class ExampleException2(Exception):
    foo = 42


class TestDuck(TestCase):

    def test_isinstance_compliant(self):
        self.assertIsInstance(Albatross(), Duck.has('wing', 'fly'))
        self.assertNotIsInstance(Ostrich(), Duck.has('wing', 'fly'))
        self.assertIsInstance(Airplain(), Duck.has('wing', 'fly'))

        ostrich_with_jetpack = Ostrich()
        ostrich_with_jetpack.fly = lambda self: 'propellant powered!'
        self.assertIsInstance(ostrich_with_jetpack, Duck.has('wing', 'fly'))

    def test_issubclass_compliaint(self):
        self.assertTrue(issubclass(Albatross, Duck.has('wing', 'fly')))
        self.assertFalse(issubclass(Ostrich, Duck.has('wing', 'fly')))
        self.assertTrue(issubclass(Airplain, Duck.has('wing', 'fly')))

    def test_duckclass_is_cached(self):
        duck = Duck.has('quack', 'walk')
        self.assertIs(duck, Duck.has('quack', 'walk'))
