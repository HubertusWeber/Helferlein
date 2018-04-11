#! /usr/bin/env python2

#
# This is a Meta-Helferlein, a Helferlein to help other Helferlein
# It is here to link all the other Helferlein into a specified directory
#

import os
import sys

helferlein = {
    "bu.py": "bu",
    "bucket.py": "bucket",
    "gg.py": "gg",
    "gp.py": "gp",
}

helferlein_path = os.path.dirname(os.path.realpath(__file__)) + "/"

for src, dst in helferlein.iteritems():
    os.system("ln -s " + helferlein_path + src + " " + sys.argv[1] + dst)
