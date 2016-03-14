#!/usr/bin/env python3
import os
import sys
import sh
import requests
import json
import socket
import getpass
sys.path.append(os.getcwd())

proto = 'https://'
apiBase =  'api.github.com/'
base = proto + apiBase

def createRepo():
    return post('user/repos',
        {
            'name' : 'Test Repo Number 1'
            ,'description' : 'Repo Description number 1'
            ,'gitignore_template':'Python'
            ,'license_template' : 'mit'
        })

def checkForKey():
    print(socket.gethostname())

def addKey(key):
    print(socket.gethostname())
    print(key)

def getToken():
    with open (".token", "r") as f:
        token = f.readline()
        if not token == "":
            return token
    with open (".token", "a+") as f:
        user = input("Please enter your github Username: ")
        password = getpass.getpass("Please enter your github Password: ")
        data = {'scopes': ['repo', 'admin:public_key'], 'note' : "A test of the authorization system", 'client_id' : "d00fbcc2e5eef2157ab3", 'client_secret' : "8fcedc3a6708bf44aeea471ee2b5516e7f227cb1", 'fingerprint' : os.getcwd()}
        r = requests.post(proto + user+':'+password+'@'+apiBase+ 'authorizations', json=data).json()
        printJ(r)
        f.write(r['token'])
        return getToken()

def getHeaders():
    return {'Authorization' : 'token ' + getToken()}

def post(url, params={}):
    return requests.post(base + url, headers=getHeaders(), json=params).json()

def get(url, params={}):
    return requests.get(base + url, headers=getHeaders(), params=params).json()

def printJ(JSON):
    print(json.dumps(JSON, indent=2))

def main():
    printJ(get('user'))
    printJ(createRepo())

if __name__ == '__main__':
    sys.exit(main())
