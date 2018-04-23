#! /usr/bin/env python2

#
# This is a Meta-Helferlein, a Helferlein to help other Helferlein
# It is here to build all the other Helferlein using cython
# and output the binaries to the specified directory
# If no directory is specified /usr/local/bin is used
# You can set the include path for the python headers via editing the include_path variable
# Alternatively you can just use the link.py Helferlein to create a symlink for every Helferlein
#

import os
import shutil
import sys

include_path = "/usr/include/python2.7"

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

build_path = os.path.join(helferlein_path, "build")

if not os.path.exists(build_path):
    os.makedirs(build_path)


for src, dst in helferlein.iteritems():
    shutil.copyfile(os.path.join(helferlein_path, src),
                    os.path.join(build_path, dst+".pyx"))

for src, dst in helferlein.iteritems():
    os.system("cython " + os.path.join(build_path, dst + ".pyx") + " --embed")

for src, dst in helferlein.iteritems():
    os.system("gcc -Os -I " + include_path + " -o " + os.path.join(output_path, dst) +
              " " + os.path.join(build_path, dst+".c") + " -lpython2.7 -lpthread -lm -lutil -ldl")

shutil.rmtree(build_path)
