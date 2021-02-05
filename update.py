#!/usr/bin/python
import subprocess

def updatesys():
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'dist-upgrade'])

def addtoolsubuntu():
    subprocess.run(['python', '-m', 'pip', 'install', '–upgrade pip'])
    subprocess.run(['apt-get', 'install', 'git'])

def githubtoolinstall():
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'update'])

def pipinstalls():
    subprocess.run(['python3', 'pip', 'install', ''])


print("V3NARI Updater by @TheCyberViking")
print("This will update to the latest build of V3NARI")
print("")
print("This will take a while go get a cookie")
print("")
print("Follow @TheCyberVIking @CyberSecStu @AlanTheBlank @Rag_Sec and @TheManyHatsClub")
print("")


updatesys()
addtoolsubuntu()
githubtoolinstall()
pipinstalls()

