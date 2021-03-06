from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

import pytest

from openpyxl25.descriptors import Strict

class TestDescriptor:

    from openpyxl25.descriptors.base import Descriptor

    class Dummy:
        pass

    def test_ctor(self):
        d = self.Descriptor('key', size=1)
        assert d.name == 'key'
        assert d.size == 1

    def test_setter(self):
        d = self.Descriptor('key')
        client = self.Dummy()
        d.__set__(client, 42)
        assert client.key == 42


@pytest.fixture
def boolean():

    from openpyxl25.descriptors.base import Bool

    class Dummy(Strict):

        value = Bool()

    return Dummy()


class TestBool:

    def test_valid(self, boolean):
        boolean.value = True
        assert boolean.value

    @pytest.mark.parametrize("value, expected",
                             [
                                 (1, True,),
                                 (0, False),
                                 ('true', True),
                                 ('false', False),
                                 ('0', False),
                                 ('f', False),
                                 ('', False),
                                 ([], False)
                             ]
                              )
    def test_cast(self, boolean, value, expected):
        boolean.value = value
        assert boolean.value == expected


def test_nested():
    from openpyxl25.descriptors.base import Bool

    class DummyNested(Strict):

        value = Bool(nested=True)

    dummy = DummyNested()
    dummy.value = True
    assert dummy.__class__.value.nested == True


@pytest.fixture
def integer():

    from openpyxl25.descriptors.base import Integer

    class Dummy(Strict):

        value = Integer()

    return Dummy()


class TestInt:

    def test_valid(self, integer):
        integer.value = 4
        assert integer.value == 4

    @pytest.mark.parametrize("value", ['a', '4.5', None])
    def test_invalid(self, integer, value):
        with pytest.raises(TypeError):
            integer.value = value

    @pytest.mark.parametrize("value, expected",
                             [
                                 ('4', 4),
                                 (4.5, 4),
                             ])
    def test_cast(self, integer, value, expected):
        integer.value = value
        assert integer.value == expected


@pytest.fixture
def float():

    from openpyxl25.descriptors.base import Float

    class Dummy(Strict):

        value = Float()

    return Dummy()


class TestFloat:

    def test_valid(self, float):
        float.value = 4
        assert float.value == 4

    @pytest.mark.parametrize("value", ['a', None])
    def test_invalid(self, float, value):
        with pytest.raises(TypeError):
            float.value = value

    @pytest.mark.parametrize("value, expected",
                             [
                                 ('4.5', 4.5),
                                 (4.5, 4.5),
                                 (4, 4.0),
                             ])
    def test_cast(self, float, value, expected):
        float.value = value
        assert float.value == expected


@pytest.fixture
def allow_none():

    from openpyxl25.descriptors.base import Float

    class Dummy(Strict):

        value = Float(allow_none=True)

    return Dummy()


class TestAllowNone:

    def test_valid(self, allow_none):
        allow_none.value = None
        assert allow_none.value is None


@pytest.fixture
def maximum():
    from openpyxl25.descriptors.base import Max

    class Dummy(Strict):

        value = Max(max=5)

    return Dummy()


class TestMax:

    def test_ctor(self):
        from openpyxl25.descriptors.base import Max

        with pytest.raises(TypeError):
            class Dummy(Strict):
                value = Max()

    def test_valid(self, maximum):
        maximum.value = 4
        assert maximum.value == 4

    def test_invalid(self, maximum):
        with pytest.raises(ValueError):
            maximum.value = 6


@pytest.fixture
def minimum():
    from openpyxl25.descriptors.base import Min

    class Dummy(Strict):

        value = Min(min=0)

    return Dummy()


class TestMin:

    def test_ctor(self):
        from openpyxl25.descriptors.base import Min

        with pytest.raises(TypeError):
            class Dummy(Strict):
                value = Min()


    def test_valid(self, minimum):
        minimum.value = 2
        assert minimum.value == 2


    def test_invalid(self, minimum):
        with pytest.raises(ValueError):
            minimum.value = -1


@pytest.fixture
def min_max():
    from openpyxl25.descriptors.base import MinMax

    class Dummy(Strict):

        value = MinMax(min=-1, max=1)

    return Dummy()


class TestMinMax:

    def test_ctor(self):
        from openpyxl25.descriptors.base import MinMax

        with pytest.raises(TypeError):

            class Dummy(Strict):
                value = MinMax(min=-10)

        with pytest.raises(TypeError):

            class Dummy(Strict):
                value = MinMax(max=10)


    def test_valid(self, min_max):
        min_max.value = 1
        assert min_max.value == 1


    def test_invalid(self, min_max):
        with pytest.raises(ValueError):
            min_max.value = 2


@pytest.fixture
def set():
    from openpyxl25.descriptors.base import Set

    class Dummy(Strict):

        value = Set(values=[1, 'a', None])

    return Dummy()


class TestValues:

    def test_ctor(self):
        from openpyxl25.descriptors.base import Set

        with pytest.raises(TypeError):
            class Dummy(Strict):

                value = Set()


    def test_valid(self, set):
        set.value = 1
        assert set.value == 1


    def test_invalid(self, set):
        with pytest.raises(ValueError):
            set.value = 2


def test_noneset():
    from openpyxl25.descriptors.base import NoneSet
    class Dummy(Strict):

        value = NoneSet(values=[1, 2, 3])

    obj = Dummy()
    obj.value = 'none'
    assert obj.value is None
    with pytest.raises(ValueError):
        obj.value = 5


@pytest.fixture
def ascii():

    from openpyxl25.descriptors.base import ASCII

    class Dummy(Strict):

        value = ASCII()

    return Dummy()


class TestASCII:

    def test_valid(self, ascii):
        ascii.value = b'some text'
        assert ascii.value == b'some text'

    value = b'\xc3\xbc'.decode("utf-8")
    @pytest.mark.parametrize("value",
                             [
                                 value,
                                 10,
                                 []
                             ]
                             )
    def test_invalid(self, ascii, value):
        with pytest.raises(TypeError):
            ascii.value = value


@pytest.fixture
def string():

    from openpyxl25.descriptors.base import String

    class Dummy(Strict):

        value = String()

    return Dummy()


class TestString:

    def test_valid(self, string):
        value = b'\xc3\xbc'.decode("utf-8")
        string.value = value
        assert string.value == value

    def test_invalid(self, string):
        with pytest.raises(TypeError):
            string.value = 5


@pytest.fixture
def Tuple():
    from openpyxl25.descriptors.base import Tuple

    class Dummy(Strict):

        value = Tuple()

    return Dummy()


class TestTuple:

    def test_valid(self, Tuple):
        Tuple.value = (1, 2)
        assert Tuple.value == (1, 2)

    def test_invalid(self, Tuple):
        with pytest.raises(TypeError):
            Tuple.value = [1, 2, 3]


@pytest.fixture
def Length():
    from openpyxl25.descriptors.base import Length

    class Dummy(Strict):

        value = Length(length=4)

    return Dummy()


class TestLength:

    def test_valid(self, Length):
        Length.value = "this"

    def test_invalid(self, Length):
        with pytest.raises(ValueError):
            Length.value = "2"
