#! /usr/bin/env python3

#
# This Helferlein searches recursively for a string in all files of a directory
#

import os
import sys


def main():
    args = str.join(" ", sys.argv[1:])
    os.system("grep -rnw . -e \"" + args + "\" --color=always")


if __name__ == '__main__':
    main()
