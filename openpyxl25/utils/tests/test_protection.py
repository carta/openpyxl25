from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

from openpyxl25.utils.protection import hash_password


def test_password():
    enc = hash_password('secret')
    assert enc == 'DAA7'
