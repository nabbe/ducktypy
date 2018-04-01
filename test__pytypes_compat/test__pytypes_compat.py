from unittest import TestCase

from pytypes import (
    typechecked,
    TypeCheckError,
    override,
    OverrideError,
)
import pytypes

from ducktypy import Duck


class Eagle(object):
    def __init__(self) -> None:
        pass

    def wing(self) -> str:
        return 'STRONG'

    def fly(self) -> bool:
        return True


class PytypesTypecheckedTest(TestCase):

    def test__pytypes_find_return_type_error(self):
        @typechecked
        def f() -> Duck.has('wing', 'fly', 'beak'):
            return Eagle()

        with self.assertRaises(TypeCheckError):
            f()

    def test__pytypes_accept_returning_duck(self):
        @typechecked
        def f() -> Duck.has('wing', 'fly'):
            return Eagle()

        f()  # SHOULD NOT RAISE

    def test__pytypes_find_input_type_error(self):
        @typechecked
        def f(bird: Duck.has('wing', 'fly', 'beak')) -> None:
            pass
        
        with self.assertRaises(TypeCheckError):
            f(Eagle())

    def test__pytypes_accept_inputting_duck(self):
        @typechecked
        def f(bird: Duck.has('wing', 'fly')) -> None:
            pass
        
        f(Eagle())  # SHOULD NOT RAISE


class C(object):

    def m1(self, d: Duck.has('a', 'b')) -> None:
        return None

    def m2(self) -> Duck.has('m1', 'm2'):
        return self


class PytypesOverrideTest(TestCase):

    def test__fail_argument_signature_mismatch(self):
        with self.assertRaises(OverrideError):
            class S1(C):
                @override
                def m1(self, d: Duck.has('a', 'b', 'c')) -> None:
                    return super().m1(d)

    def test__pass_argument_signatuire_matches(self):
        class S1(C):
            @override
            def m1(self, d: Duck.has('a')) -> None:
                return None

    def test__fail_returntype_signature_mismatch(self):
        with self.assertRaises(OverrideError):
            class S2(C):
                @override
                def m2(self) -> Duck.has('m1'):
                    return self

    def test__fail_returntype_signature_match(self):
        class S2(C):
            @override
            def m2(self) -> Duck.has('m1', 'm2', 'm3'):
                return self
