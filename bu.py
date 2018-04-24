#! /usr/bin/env python3

#
# This Helferlein updates / upgrades all tools that need it mainly (as the name implies) homebrew
# It can be called with a specific tool as command line argument or "alle" to update / upgrade everything
#

import os
from pip import _internal as pip
import sys


def brew():
    print("brew update")
    os.system("brew update")
    print("brew upgrade")
    os.system("brew upgrade")
    print("brew cleanup")
    os.system("brew cleanup")
    print("brew cask upgrade")
    os.system("brew cask upgrade")
    print("brew cask clean")
    os.system("brew cask cleanup")


def tldr():
    print("updating tldr")
    os.system("tldr --update")


def npm():
    print("upgrade/update npm")
    os.system("npm up")


def my_pip():
    print("upgrade pip3 itself")
    os.system("pip3 install --upgrade pip")
    print("upgrade pip3 packages")
    packages = [dist.project_name for dist in pip.get_installed_distributions()]
    os.system("pip3 install --upgrade " + ' '.join(packages))


def alle():
    brew()
    tldr()
    npm()
    my_pip()


commands = {
    "brew": brew,
    "tldr": tldr,
    "npm": npm,
    "pip": my_pip,
    "alle": alle,
}


def help_message():
    print("Specify what to do")
    print("Options are:")
    for command in commands:
        print(command)


try:
    commands[sys.argv[1]]()
except:
    help_message()
    exit(2)
