import PyWave
import argparse
import os.path
import glob
import xml.etree.ElementTree as Etree
from typing import List, Tuple

# Patch PyWave to support Latin1 in metadata strings
PyWave.clstr = lambda bytes_: bytes_.replace(b'\x00', b'')


def cmd_parse(*args):
    parser = argparse.ArgumentParser(description='Automatic dump of a playlist.')
    parser.add_argument('-d', '--dir', help='Process a directory instead of a playlist', action='store_true')
    parser.add_argument('infile', help='input file (expected to be a wpl playlist file or a folder)')
    parser.add_argument('outfile', nargs='?', default=None, help='output file (default=standard output)')
    parser.add_argument('-s', '--sep', help='Separator between name and duration (default \\t)')
    return parser.parse_args(args)


def wav_data(file: str) -> Tuple[str, int]:
    with PyWave.Wave(file) as wav:
        duration = round(wav.samples / wav.samples_per_sec)
        try:
            name = wav.metadata['INFO']['INAM']
            try:
                name = name.decode()
            except UnicodeError:
                name = name.decode('Latin1')
        except KeyError:
            name = os.path.splitext(os.path.basename(file))[0]
    return name, duration


class WplParser:
    def __init__(self, infile: str, outfile: str = None, in_dir: bool = False, sep: str = '\t'):
        self.infile = infile
        self.outfile = outfile
        self.in_dir = in_dir
        self.sep = sep

    def wpl_list(self) -> List[str]:
        folder = os.path.dirname(self.infile)
        with open(self.infile, encoding='utf-8') as wpl:
            return [os.path.normpath(os.path.join(folder, elt.attrib['src']))
                    for elt in Etree.parse(wpl).findall('.//media')]

    def dir_list(self) -> List[str]:
        lst = glob.glob(os.path.join(os.path.normpath(self.infile), '*.WAV'))
        lst.sort()
        return lst

    def list(self) -> List[Tuple[str, int]]:
        wav_lst = self.dir_list() if self.in_dir else self.wpl_list()
        return [wav_data(file) for file in wav_lst]

    def write(self, fd):
        for name, duration in self.list():
            mn, sec = divmod(duration, 60)
            print(name, f'{mn}:{sec:02d}', sep=self.sep, file=fd)

    def run(self):
        if self.outfile:
            with open(self.outfile, 'w') as fd:
                self.write(fd)
        else:
            self.write(None)


def _run():
    import sys
    args = cmd_parse(*sys.argv[1:])
    WplParser(args.infile, args.outfile, args.dir, args.sep).run()
