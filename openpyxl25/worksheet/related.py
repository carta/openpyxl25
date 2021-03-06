from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl

from openpyxl25.descriptors.serialisable import Serialisable
from openpyxl25.descriptors.excel import Relation


class Related(Serialisable):

    id = Relation()


    def __init__(self, id=None):
        self.id = id


    def to_tree(self, tagname, idx=None):
        return super(Related, self).to_tree(tagname)
