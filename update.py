#!/usr/bin/python
import subprocess

def updatesys():
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'upgrade'])
    subprocess.run(['apt-get', 'dist-upgrade'])

def addtoolsubuntu():
    subprocess.run(['python', '-m', 'pip', 'install', '–upgrade pip'])

def githubtoolinstall():
    subprocess.run(['git clone https://github.com/DedSecInside/TorBot.git'])
    subprocess.run(['cd TorBot'])
    subprocess.run(['pip3 install -r requirements.txt'])
    subprocess.run(['./install.sh'])
    subprocess.run(['cd ..'])



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
print("All Done Enjoy")
