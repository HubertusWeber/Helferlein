#! /usr/bin/env python3

#
# This Helferlein searches recursively for a string in all files of a directory
#

import os
import sys

args = str.join(" ", sys.argv[1:])

os.system("grep -rnw . -e \"" + args + "\" --color=always")
