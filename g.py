#! /usr/bin/env python

import os
import string
import sys

os.system('grep -rnw . -e "' +
          string.join(sys.argv[1:], ' ') + '" --color=always')
