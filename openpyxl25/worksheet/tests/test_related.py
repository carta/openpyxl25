from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

import pytest
from openpyxl25.tests.helper import compare_xml

from openpyxl25.xml.functions import tostring


def test_related():
    from openpyxl25.worksheet.related import Related
    rel = Related(id="rId1")
    expected = """
    <drawing xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="rId1"/>
    """
    xml = tostring(rel.to_tree("drawing"))
    diff = compare_xml(xml, expected)
    assert diff is None, diff
