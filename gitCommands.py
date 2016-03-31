#!/usr/bin/env python3
import os
import sys
import sh
from sh import git
import requests
import json
sys.path.append(os.getcwd())
import sshCommands
import editCommands

def init(template=False):
    """ Creates a new repository, copying the default template if one is provided."""
    if ( template ) :
        git.init("--template", template)
    else :
        git.init()

def add():
    """ Adds files to the staging area. This will not commit them, just tell git that this version of the file should be committed"""
    return git.add("-A")

def isRepo():
    """ Returns if the cwd is a git repo """
    try:
        git("rev-parse", "--is-inside-work-tree")
        return 1
    except:
        return 0

def branchName():
    return git("rev-parse", "--abbrev-ref", "HEAD")

def commit(message=False):
    if not message :
        message = editCommands(str(branchName()) + " : ")
    print("git commit -m " + message)
    try : git.commit(m=message)
    except : print("Nothing to commit")

def save(message=False):
    add()
    commit(message)

def addRemote(url, name="gh", fetch=False):
    if fetch :
        print("git remote add " + name + " https://github.com/" + url +".git"+ " -f")
        try: return git.remote.add(name, "https://github.com/" + url + ".git", "-f")
        except: print("Remote already exists")
    else :
        print("git remote add " + name + " https://github.com/" + url +".git")
        try: return git.remote.add(name, "https://github.com/" + url + ".git")
        except: print("Remote already exists")

def clone(url):
        git.clone(url, "./")

def fetch():
    print("git fetch")
    return git.fetch()

def pushAll(message=False):
    save(message)
    push()

def push():
    print("git push")
    try: git.push()
    except:
        try:
            branch_name = branchName()
            print("git push -u gh " + branch_name)
            try: git.push("-u", "gh", branch_name)
            except : print("Nothing to push")
        except: print("Nothing has been created")

def branch(name):
    try: git.checkout(name)
    except: git.checkout("-b", name)

def branchVerify(name):
    return git.branchVerify("rev-parse", "--verify", name)

def pagesBranch():
    try:
        git.checkout("--orphan", "gh-pages")
        git.rm("-r", "-f", "--ignore-unmatch", ".")
    except: print("No files exist in the gh-pages branch")
    try: sh.cp("-R", os.path.dirname(os.path.realpath(__file__)) + "/www/coming-soon/*", "./")
    except: print("Template not found")
    pushAll("Creating the first instance of the coming-soon site")
    try: git.checkout("dev")
    except: git.checkout("-b", "dev")

def cloneWiki(name, cloneUrl):
    sh.cd("../")
    sh.mkdir(name + ".wiki")
    sh.cd(name + ".wiki")
    git.init()
    try:
        git.remote.add(name, cloneUrl[:-4]+ ".wiki.git")
        sh.touch("home.md")
        pushAll("Initial Wiki commit")
    except: print("Wiki remote already exists")
    sh.cd("../" + name)

def main(args):
    {
        'save' : save,
        'add' : add,
        'commit' : commit,
        'branch' : branch,
        'isRepo' : isRepo,
        'branchName' : branchName
    }[args[0]]()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
