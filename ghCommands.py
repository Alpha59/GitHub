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
tokenFile = os.path.dirname(os.path.realpath(__file__)) + '/.token'

def checkForKey():
    print(socket.gethostname())

def addKey(key):
    print(socket.gethostname())
    print(key)

def deleteToken():
    with open (tokenFile, "w") as f:
        token = f.write("")
    pass

def getToken():
    with open (tokenFile, "r") as f:
        token = f.readline()
        if not token == "":
            return token
    with open (tokenFile, "a+") as f:
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
    try :
        resp = requests.post(base + url, headers=getHeaders(), json=params)
        return resp.json()
    except :
        print("Error with Post Request")

def get(url, params={}):
    try :
        resp = requests.get(base + url, headers=getHeaders(), params=params)
        return resp.json()
    except :
        print("Error with Get Request")

def printJ(JSON):
    print(json.dumps(JSON, indent=2))

if __name__ == '__main__':
    sys.exit(main())

def main():
    printJ(get('user/repos'))

##############################################################################

def create(dirName, desc) :
    print("gitHub.post('user/repos')")
    return post('user/repos',
        {
            'name' : dirName
            ,'description' : desc
            ,'homepage' : proto + getUsername() + '.github.io/' + dirName
            ,'has_issues' : 'true'
            ,'has_wiki' : 'true'
            ,'has_downloads' : 'true'
        })

def getUsername() :
    print("gitHub.get('user')['login']")
    return get('user')['login'].lower()

def isRepo(dirName) :
    print("gitHub.get('user/repos').find(dirName)")
    repos = get('user/repos')
    for repo in repos :
        if repo['name'] == dirName :
            return repo
