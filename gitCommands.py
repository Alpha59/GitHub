#!/usr/bin/env python3
import os
import sys
from sh import git
import requests
import json
sys.path.append(os.getcwd())

def add():
    git.add("-A")

def commit():
    message = input("Enter A message: " )
    git.commit(m=message)

def save():
    add()
    commit()

def main():
    save()

if __name__ == '__main__':
    sys.exit(main())
