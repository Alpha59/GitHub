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
    if args[0] :
        message = args[0]
    else :
        message = input("Enter A message: " )
    print("git commit -m " + message)
    git.commit(m=message)

def save(args=[]):
    add()
    commit()

def addRemote(url, name="gh", fetch=0):
    if fetch :
        print("git remote add " + name + " https://github.com/" + url + " -f")
        return git.remote.add(name, "https://github.com/" + url, "-f")
    else :
        print("git remote add " + name + " https://github.com/" + url)
        return git.remote.add(name, "https://github.com/" + url)

def clone(url, dirName=""):
    if dirName == "" :
        return git.clone(url)
    else :
        return git.clone(url, dirName)

def fetch():
    print("git fetch")
    return git.fetch()

def pushAll():
    save()
    push()

def push():
    print("git push")
    try: git.push()
    except:
        branchName = git("rev-parse", "--abbrev-ref", "HEAD")
        print("git push -u gh " + branchName)
        git.push("-u", "gh", branchName)

def branch(args):
    try: git.checkout("FB-" + args[0])
    except: git.checkout("-b", "FB-" + args[0])

def branchVerify(name):
    return git.branchVerify("rev-parse", "--verify", name)

def pagesBranch():
    git.checkout("--orphan", "gh-pages")
    git.rm("-rf")
    sh.cp("-R", os.path.dirname(os.path.realpath(__file__)) + "/comingSoon/template1/*", "./")
    save()
    git.push("gh", "gh-pages")

def cloneWiki(cloneUrl):
    sh.cd("../")
    git.clone(cloneUrl[:-4]+ ".wiki.git")

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
