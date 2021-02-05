#!/usr/bin/python
import subprocess

def updatesys():
    subprocess.run(['apt-get', 'update', '-y'])
    subprocess.run(['apt-get', 'upgrade', '-y'])
    subprocess.run(['apt-get', 'dist-upgrade', '-y'])

def addtoolsubuntu():
    subprocess.run(['apt-get', 'install', 'python3-pip', '-y'])
    subprocess.run(['python', '-m', 'pip', 'install', '–upgrade pip', '-y'])
    subprocess.run(['apt-get', 'install', 'git', '-y'])
    subprocess.run(['apt-get', 'install', 'git-core', 'git-gui', 'git-doc', '-y'])
    
def githubtoolinstall():
    subprocess.run(['git', 'clone', 'https://github.com/DedSecInside/TorBot.git'])
    subprocess.run(['pip3', 'install', '-r', 'TorBot/requirements.txt'])
    subprocess.run(['./TorBot/install.sh', '-y'])

    
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
