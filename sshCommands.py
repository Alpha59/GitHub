#!/usr/bin/env python3
import os
import sys
import sh
import requests
import json
sys.path.append(os.getcwd())

from os.path import expanduser
import ghCommands as gitHub

home = expanduser("~") + '/'
ssh_path = home + 'Test/.ssh/'

def checkForKey():
    try:
        keyName = sh.grep(sh.ls("-a", "-l", ssh_path), "[a-z\-_1-9]*\.pub", "-o").strip()
        return keyName
    except:
        return None

def genKey(keyName):
    email = input("Enter your github email please: " )
    password = input("Enter your github password please: ")
    sh.ssh.keygen(t="rsa", b="4096", C=email, N=password, f=ssh_path+keyName)

def exportToGH(keyName='id_rsa.pub2') :
    gitHub.checkForKey()
    os.system('ssh-agent -s')
    #sh.ssh.add(ssh_path + keyName)
    key = sh.cat(ssh_path + keyName)
    gitHub.addKey(key)

def addKey():
    keyName = checkForKey()
    if keyName == None :
        keyName = genKey('id_rsa')
    exportToGH(keyName)

def main():
    addKey()

if __name__ == '__main__':
    sys.exit(main())
