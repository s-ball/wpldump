from .wpldump import WplParser, cmd_parse
import sys


def run():
    args = cmd_parse(*sys.argv[1:])
    WplParser(args.infile, args.outfile, args.dir, args.sep).run()


run()