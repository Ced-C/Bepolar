# Script should run in root `sudo python3 install bepolar`

# # a la place 
# - copier fichier en .bk
# - copier fichier en .old
# - faire `sudo xkalamine install`
# - faire modifications .old et remplacer fichier 
# - supprimer fichier old

import shutil
import subprocess
import os
from bs4 import BeautifulSoup

# Global variables
name = 'bepolar'
desc = 'French (Bepolar)'

path = "/usr/share/X11/xkb/rules/"
rules = ['base.xml', 'evdev.xml']

# copy files to modify
for xml in rules:
    shutil.copyfile(path+xml, path+xml+'.tmp')

try:
    subprocess.run(
        "xkalamine install " +\
        os.path.dirname(__file__) +\
        '/../Bepolar.yml',
        shell=True, check=True,
        capture_output=True, encoding='utf-8'
    )
except subprocess.CalledProcessError as e:
    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

# open/modify the `tmp` copyied files and replace original xml
for xml in rules:
    with open( path+xml+'.tmp', 'r') as f:
        file = f.read() 
    soup = BeautifulSoup(file, 'xml')

    for layout in soup.find_all('layout'):
       for variant in layout.findChildren("name" , recursive=True):
           if variant.string == 'bepo':
                new_layout = BeautifulSoup(
                    f'''<variant>
                        <configItem>
                            <name>{name}</name>
                            <description>{desc}</description>
                        </configItem>
                    </variant>''',
                    'xml')
                variant.parent.parent.insert_after(new_layout)
    
    with open( path+xml, 'w') as f_out:
        print(soup.prettify(), file=f_out)
