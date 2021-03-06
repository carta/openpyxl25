from __future__ import absolute_import
# Copyright (c) 2010-2017 openpyxl
from openpyxl25.compat import unicode

from openpyxl25.descriptors.serialisable import Serialisable
from openpyxl25.descriptors import (
    Sequence,
    Alias
)


class AuthorList(Serialisable):

    tagname = "authors"

    author = Sequence(expected_type=unicode)
    authors = Alias("author")

    def __init__(self,
                 author=(),
                ):
        self.author = author
