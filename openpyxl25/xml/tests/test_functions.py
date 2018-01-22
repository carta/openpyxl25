import pytest
try:
    from xml.etree.cElementTree import ParseError
except ImportError:
    # py26
    ParseError = SyntaxError

def test_safe_iterator_none():
    from openpyxl25.xml.functions import safe_iterator
    seq = safe_iterator(None)
    assert seq == []


@pytest.mark.parametrize("xml, tag",
                         [
                             ("<root xmlns='http://openpyxl25.org/ns' />", "root"),
                             ("<root />", "root"),
                         ]
                         )
def test_localtag(xml, tag):
    from openpyxl25.xml.functions import localname
    from openpyxl25.xml.functions import fromstring
    node = fromstring(xml)
    assert localname(node) == tag


@pytest.mark.lxml_required
def test_dont_resolve():
    from openpyxl25.writer.functions import fromstring
    s = b"""<?xml version="1.0" encoding="ISO-8859-1"?>
            <!DOCTYPE foo [
            <!ELEMENT foo ANY >
            <!ENTITY xxe SYSTEM "file:///dev/random" >]>
            <foo>&xxe;</foo>"""
    node = fromstring(s)


@pytest.mark.no_lxml
def test_dont_resolve():
    from openpyxl25.writer.functions import fromstring
    s = b"""<?xml version="1.0" encoding="ISO-8859-1"?>
            <!DOCTYPE foo [
            <!ELEMENT foo ANY >
            <!ENTITY xxe SYSTEM "file:///dev/random" >]>
            <foo>&xxe;</foo>"""
    with pytest.raises(ParseError):
        node = fromstring(s)
