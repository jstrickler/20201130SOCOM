#  python fauxgrep.py -i -n PATTERN file1 file2 ...
import sys
import fileinput
import argparse
import re

parser = argparse.ArgumentParser(description="Faux grep")

parser.add_argument('-i', dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument('-n', dest="show_file_name", action="store_true", help="show file name")
parser.add_argument('pattern', help="pattern to find")
parser.add_argument('files', nargs="*", help="files to search (STDIN if none)")

args = parser.parse_args()

# print(args)
rx_pattern = re.compile(args.pattern, re.I if args.ignore_case else 0)


for raw_line in fileinput.input(args.files):
    if rx_pattern.search(raw_line):
        line = raw_line.rstrip()  # remove \n
        if args.show_file_name:
            print(fileinput.filename(), end=' ')
        print(line)




