#! /usr/bin/env python3

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


def main():
    helferlein_path = os.path.dirname(os.path.realpath(__file__)) + "/"
    if len(sys.argv) < 2:
        output_path = "/usr/local/bin/"
    else:
        output_path = sys.argv[1]
    for src, dst in helferlein.items():
        src_path = os.path.join(helferlein_path, src)
        dst_path = os.path.join(output_path, dst)
        try:
            os.remove(dst_path)
        except OSError:
            pass
        os.system("ln -s " + src_path + " " + dst_path)


if __name__ == '__main__':
    main()
