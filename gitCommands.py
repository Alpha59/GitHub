#!/usr/bin/env python3
import os
import sys
from sh import git
import requests
import json
sys.path.append(os.getcwd())
import sshCommands

def add(args=[]):
    git.add("-A")

def init(args=[]):
    git.init()

def isRepo(args=[]):
    try:
        git("rev-parse", "--is-inside-work-tree")
        return 1
    except:
        return 0

def commit(args=[]):
    if ( len(args) > 0 ) :
        message = args[0]
    else :
        message = input("Enter A message: " )
    git.commit(m=message)

def save(args=[]):
    add()
    commit()

def addRemote():
    pass

def clone():
    pass

def fetch():
    pass

def pushAll():
    pass

def branch(args):
    git.checkout("-b", "FB-" + args[0])

def main(args):
    {
        'save' : save,
        'add' : add,
        'commit' : commit,
        'branch' : branch,
        'isRepo' : isRepo
    }[args[0]](args[1:])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
