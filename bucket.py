#! /usr/bin/env python2

#
# This Helferlein adds a backup remote with the name bitbucket to a git repo
#

import os
import sys

os.system("git remote add bitbucket " + sys.argv[1])
os.system("git push --mirror bitbucket")
