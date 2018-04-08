#! /usr/bin/env python

#
# This Helferlein searches recursively for a string in all files of a directory
#

import os
import string
import sys

os.system('grep -rnw . -e "' +
          string.join(sys.argv[1:], ' ') + '" --color=always')
