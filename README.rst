Namespaced OpenPyXL2.5
======================

This branch changes the namespace of openpyxl to allow for incremental upgrades of applications using the library.

Remote Origin
    - :code:`git remote add hg-origin hg::https://bitbucket.org/openpyxl/openpyxl` 

OpenPyXL's Main Repo is mercurial. A special plugin is needed to update from upstream
    - :code:`brew install git-remote-hg`

To Update:
    - :code:`git fetch`
    - :code:`git pull hg-origin master`
    - :code:`git gc --aggressive`
    - :code:`git push`


openpyxl
========

openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

It was born from lack of existing library to read/write natively from Python
the Office Open XML format.

All kudos to the PHPExcel team as openpyxl was initially based on `PHPExcel
<http://www.phpexcel.net/>`_


Mailing List
============

Official user list can be found on
http://groups.google.com/group/openpyxl-users


Sample code::

    from openpyxl import Workbook
    wb = Workbook()

    # grab the active worksheet
    ws = wb.active

    # Data can be assigned directly to cells
    ws['A1'] = 42

    # Rows can also be appended
    ws.append([1, 2, 3])

    # Python types will automatically be converted
    import datetime
    ws['A2'] = datetime.datetime.now()

    # Save the file
    wb.save("sample.xlsx")


Official documentation
======================

The documentation is at: https://openpyxl.readthedocs.io

* installation methods
* code examples
* instructions for contributing

Release notes: https://openpyxl.readthedocs.io/en/latest/changes.html
