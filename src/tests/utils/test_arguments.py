import os

from argparse import Namespace

from code.utils.arguments import get_parser, get_files_list


def test_get_parser():
    """ Tests if reading args is working """
    res = get_parser()
    assert isinstance(res, Namespace)


def test_get_files_list():
    """ Tests if is returning a list with files """
    files = get_files_list("./raw_csv/")
    for file in files:
        assert os.path.isfile(file)