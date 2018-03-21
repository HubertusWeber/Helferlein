#! /usr/bin/env python

import os
import sys


def fefe():
    print "Pulling New Version"
    os.system("cd ~/GitHub/Fefes-Server/; git pull")
    print "Restarting Server"
    os.system("~/GitHub/Fefes-Server/fefe.py restart")


def hw():
    print "Pulling New Version"
    os.system("cd ~/GitHub/hawegegeServer/; git pull")
    print "Restarting Server"
    os.system("~/GitHub/hawegegeServer/hawegege.py restart")


servers = {
    "hw": hw,
    "fefe": fefe,
}


def help_message():
    print "Specify which server to update"
    print "Options are:"
    for server in servers:
        print server


try:
    servers[sys.argv[1]]()
except:
    help_message()
    exit(2)
