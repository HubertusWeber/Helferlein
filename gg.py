#! /usr/bin/env python2

#
# This Helferlein is my very own personal updator
# First it pulls the newest version of the specified project from GitHub
# Then it executes the runscript of that project with the restart option
# Currently supports hw and fefe with more to come as I get busy
# If you are reading this: Thank you so much for showing interest in my code <3
# BUT this Helferlein is probably absolutely useless to you ;D
#

import os
import sys


def fefe():
    print("Pulling New Version")
    os.system("cd ~/GitHub/Fefes-Server/; git pull")
    print("Restarting Server")
    os.system("~/GitHub/Fefes-Server/fefe.py restart")


def hw():
    print("Pulling New Version")
    os.system("cd ~/GitHub/hawegegeServer/; git pull")
    print("Restarting Server")
    os.system("~/GitHub/hawegegeServer/hawegege.py restart")


servers = {
    "hw": hw,
    "fefe": fefe,
}


def help_message():
    print("Specify which server to update")
    print("Options are:")
    for server in servers:
        print(server)


try:
    servers[sys.argv[1]]()
except:
    help_message()
    exit(2)
