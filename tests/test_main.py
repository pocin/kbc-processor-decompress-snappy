"""
Some tests
"""
import os
import logging
import pytest
from main import _build_outpath_from_inpath, find_all_files, process_file


THIS_FILE = os.path.dirname(os.path.abspath(__file__))

def test_building_outpaths():
    tests = [
        ('/data/in/files/something.xls', '/data/out/files/something'),
        ('/data/in/files/something.csv.snappy', '/data/out/files/something.csv'),
        ('/data/in/files/nested/deeply/something', '/data/out/files/nested/deeply/something')
    ]
    for inpath, expected in tests:
        assert _build_outpath_from_inpath(inpath) == expected

def test_finding_files():
    files = set(find_all_files(THIS_FILE.rstrip('/')+ '/data'))
    def pj(fname):
        return os.path.join(THIS_FILE, 'data/in/files', fname)
    assert pj('decompress_this.snappy') in files


def test_decompressing(tmpdir):
    inpath = os.path.join(THIS_FILE,  'data/in/files/decompress_this.snappy')
    outpath = tmpdir.mkdir('out').join('decompress_this')

    out = process_file(inpath, outpath.strpath)
    with open(out) as f:
        decompressed = f.read()

    expected = """what,who
Hello,World"""
    assert decompressed == expected
