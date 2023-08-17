#/bin/python3
from bs4 import BeautifulSoup
import re

# Remove attribute `type=kalamine` from rules files
path = "/usr/share/X11/xkb/rules/"
for xml in ['base.xml', 'evdev.xml']:
    with open(path+xml, 'r') as f:
        file = f.read() 
    s = BeautifulSoup(file, 'xml')
    for kalamine in s.find_all("variant",{'type':'kalamine'}):
        del kalamine['type']
    with open(path+xml, 'w') as f_out:
        print(s.prettify(), file=f_out)

# Remove `KALAMINE::BEPOLAR::BEGIN` & `KALAMINE::BEPOLAR::END` from fr file
path = "/usr/share/X11/xkb/symbols/"
 
with open(path+'fr','r') as file:
    lines = file.readlines()

with open(path+'fr','w') as file:
    for line in lines:
        x = re.findall("^// KALAMINE::", line)
        if not x:
            file.write(line)
