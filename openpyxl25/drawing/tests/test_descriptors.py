from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

import pytest

from openpyxl25.xml.functions import fromstring, tostring
from openpyxl25.tests.helper import compare_xml


def test_color_descriptor():
    from openpyxl25.drawing.colors import ColorChoiceDescriptor

    class DummyStyle(object):

        value = ColorChoiceDescriptor('value')

    style = DummyStyle()
    style.value = "efefef"
    style.value.RGB == "efefef"
