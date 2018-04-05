"""
Decompress snappy files
"""
import logging
import os
import sys
import glob
import snappy


def find_all_files(datadir):
    logging.info("Looking for files in '%s'", datadir)
    for path in glob.iglob(os.path.join(datadir, '**/*'), recursive=True):
        if os.path.isfile(path):
            yield path


def _build_outpath_from_inpath(inpath):
    logging.debug("Buliding outpath from %s", inpath)
    infolder, name = os.path.split(inpath)
    outfolder = infolder.replace('/data/in/files', '/data/out/files')
    if not os.path.isdir(outfolder):
        os.makedirs(outfolder)
    basename, _ = os.path.splitext(name)
    outpath = os.path.join(outfolder, basename)
    logging.debug("destination is %s", outpath)
    return outpath

def process_file(inpath, outpath):
    """Decompress snappy file into destination
    """
    logging.debug("Parsing %s into %s", inpath, outpath)
    with open(inpath, 'rb') as fin, open(outpath, 'wb') as fout:
        snappy.stream_decompress(fin, fout)
    return outpath

def main(datadir):
    for inpath in find_all_files(datadir):
        outpath = _build_outpath_from_inpath(inpath)
        process_file(inpath, outpath)


if __name__ == "__main__":
    try:
        if os.getenv("KBC_PARAMETER_DEBUG"):
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        else:
            logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        logging.debug("Starting processor")
        main('/data/in/files/')
    except (ValueError, KeyError, snappy.UncompressError) as err:
        logging.exception(err)
        sys.exit(1)
    except:
        logging.exception("Internal error")
        sys.exit(2)
