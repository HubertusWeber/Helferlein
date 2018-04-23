#! /usr/bin/env python2

#
# This is a Meta-Helferlein, a Helferlein to help other Helferlein
# It is here to link all the other Helferlein into a specified directory
# If no directory is specified /usr/local/bin is used
#

import os
import sys

helferlein = {
    "abs.py": "abs",
    "bu.py": "bu",
    "bucket.py": "bucket",
    "gg.py": "gg",
    "gp.py": "gp",
}

helferlein_path = os.path.dirname(os.path.realpath(__file__)) + "/"

if len(sys.argv) < 2:
    output_path = "/usr/local/bin/"
else:
    output_path = sys.argv[1]

for src, dst in helferlein.iteritems():
    os.system("ln -s " + os.path.join(helferlein_path, src) +
              " " + os.path.join(output_path, dst))
