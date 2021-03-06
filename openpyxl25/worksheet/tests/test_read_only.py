from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

import pytest

from openpyxl25.xml.functions import fromstring, tostring
from openpyxl25.tests.helper import compare_xml


class DummyWorkbook:

    excel_base_date = None
    sheetnames = []


@pytest.fixture
def ReadOnlyWorksheet():
    from openpyxl25.worksheet.read_only import ReadOnlyWorksheet
    return ReadOnlyWorksheet


class TestReadOnlyWorksheet:

    def test_from_xml(self, datadir, ReadOnlyWorksheet):

        datadir.chdir()

        ws = ReadOnlyWorksheet(DummyWorkbook(), "Sheet", "", "sheet_inline_strings.xml", [])
        cells = tuple(ws.get_squared_range(1, 1, 1, 1))
        assert len(cells) == 1
        assert cells[0][0].value == "col1"
