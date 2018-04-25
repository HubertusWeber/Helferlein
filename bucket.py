#! /usr/bin/env python3

#
# This Helferlein adds a backup remote with the name bitbucket to a git repo
#

import os
import sys


def main():
    os.system("git remote add bitbucket " + sys.argv[1])
    os.system("git push --mirror bitbucket")


if __name__ == '__main__':
    main()
