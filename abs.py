#! /usr/bin/env python3

#
# This Helferlein returns the absolute path of every file or directory given to it
# If nothing is provided, it simply returns the current working directory
#

import os
import sys

if len(sys.argv) > 1:
    print(os.path.abspath(sys.argv[1]))
else:
    print(os.getcwd())
