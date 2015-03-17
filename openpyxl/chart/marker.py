#Autogenerated schema

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Typed,
    Float,
    MinMax,
    Bool,
    Set,
    NoneSet,
    String,
    Integer,)

from openpyxl.descriptors.excel import(
    Coordinate,
    Percentage,
    HexBinary,
    TextPoint,
    ExtensionList,
)
from .layout import Layout
from .shapes import *
from .text import *
from .error_bar import *



class PictureStackUnit(Serialisable):

    val = Typed(expected_type=Float())

    def __init__(self,
                 val=None,
                ):
        self.val = val


class PictureFormat(Serialisable):

    val = Set(values=(['stretch', 'stack', 'stackScale']))

    def __init__(self,
                 val=None,
                ):
        self.val = val


class PictureOptions(Serialisable):

    applyToFront = Bool(allow_none=True, nested=True)
    applyToSides = Bool(allow_none=True, nested=True)
    applyToEnd = Bool(allow_none=True, nested=True)
    pictureFormat = Typed(expected_type=PictureFormat, allow_none=True)
    pictureStackUnit = Typed(expected_type=PictureStackUnit, allow_none=True)

    def __init__(self,
                 applyToFront=None,
                 applyToSides=None,
                 applyToEnd=None,
                 pictureFormat=None,
                 pictureStackUnit=None,
                ):
        self.applyToFront = applyToFront
        self.applyToSides = applyToSides
        self.applyToEnd = applyToEnd
        self.pictureFormat = pictureFormat
        self.pictureStackUnit = pictureStackUnit


class UnsignedInt(Serialisable):

    val = Typed(expected_type=Integer, )

    def __init__(self,
                 val=None,
                ):
        self.val = val


class Marker(Serialisable):

    symbol = Set(values=(['circle', 'dash', 'diamond', 'dot', 'none', 'picture', 'plus', 'square', 'star', 'triangle', 'x', 'auto']), nested=True)
    size = MinMax(min=2, max=72, nested=True)
    spPr = Typed(expected_type=ShapeProperties, allow_none=True)
    extLst = Typed(expected_type=ExtensionList, allow_none=True)

    def __init__(self,
                 symbol=None,
                 size=None,
                 spPr=None,
                 extLst=None,
                ):
        self.symbol = symbol
        self.size = size
        self.spPr = spPr
        self.extLst = extLst


class DPt(Serialisable):

    idx = Typed(expected_type=UnsignedInt, )
    invertIfNegative = Bool(allow_none=True, nested=True)
    marker = Typed(expected_type=Marker, allow_none=True)
    bubble3D = Bool(allow_none=True, nested=True)
    explosion = Typed(expected_type=UnsignedInt, allow_none=True)
    spPr = Typed(expected_type=ShapeProperties, allow_none=True)
    pictureOptions = Typed(expected_type=PictureOptions, allow_none=True)
    extLst = Typed(expected_type=ExtensionList, allow_none=True)

    def __init__(self,
                 idx=None,
                 invertIfNegative=None,
                 marker=None,
                 bubble3D=None,
                 explosion=None,
                 spPr=None,
                 pictureOptions=None,
                 extLst=None,
                ):
        self.idx = idx
        self.invertIfNegative = invertIfNegative
        self.marker = marker
        self.bubble3D = bubble3D
        self.explosion = explosion
        self.spPr = spPr
        self.pictureOptions = pictureOptions
        self.extLst = extLst
