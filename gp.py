#! /usr/bin/env python2

#
# This Helferlein iterates over a given (or the current) directory
# and calls git pull in every subdirectory
#

import os
import sys
import time

if len(sys.argv) > 1:
    working_dir = os.path.abspath(sys.argv[1])
else:
    working_dir = os.getcwd()

for repo in os.listdir(working_dir):
    directory = os.path.join(working_dir, repo)
    if os.path.isdir(directory):
        sys.stdout.write(repo + "\t")
        sys.stdout.flush()
        os.system("cd " + directory + "; git pull")
