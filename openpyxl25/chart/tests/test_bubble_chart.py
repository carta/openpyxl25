from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

import pytest

from openpyxl25.xml.functions import fromstring, tostring
from openpyxl25.tests.helper import compare_xml

@pytest.fixture
def BubbleChart():
    from openpyxl25.chart.bubble_chart import BubbleChart
    return BubbleChart


class TestBubbleChart:

    def test_ctor(self, BubbleChart):
        bubble_chart = BubbleChart()
        xml = tostring(bubble_chart.to_tree())
        expected = """
        <bubbleChart>
          <axId val="10" />
          <axId val="20" />
        </bubbleChart>
        """
        diff = compare_xml(xml, expected)
        assert diff is None, diff


    def test_from_xml(self, BubbleChart):
        src = """
        <bubbleChart>
          <axId val="10" />
          <axId val="20" />
        </bubbleChart>
        """
        node = fromstring(src)
        bubble_chart = BubbleChart.from_tree(node)
        assert dict(bubble_chart) == {}
