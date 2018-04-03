#! /usr/bin/env python

import os
import sys

os.system("git remote add bitbucket " + sys.argv[1])
os.system("git push --mirror bitbucket")
