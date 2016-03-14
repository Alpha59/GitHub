#!/usr/bin/env python3
import os
import sys
from sh import git
import requests
import json
sys.path.append(os.getcwd())

def add(args=[]):
    git.add("-A")

def commit(args=[]):
    message = input("Enter A message: " )
    git.commit(m=message)

def save(args=[]):
    add()
    commit()

def branch(args):
    git.checkout("-b", "FB-" + args[0])

def main(args):
    {
        'save' : save,
        'add' : add,
        'commit' : commit,
        'branch' : branch
    }[args[0]](args[1:])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
