#/bin/python3
import re

# Remove attribute `type="kalamine"` from rules files
path = "/usr/share/X11/xkb/rules/"
for xml in ['base.xml', 'evdev.xml']:
    with open(path+xml,'r') as file:
        lines = file.readlines()
    with open(path+xml,'w') as file:
        for line in lines:
            if line.find('<variant type="kalamine">') == -1:
                file.write(line)
            else:
                file.write(
                    line.replace('<variant type="kalamine">', '<variant>')
                )
print('`xkb/rules` files updated : `type="kalamine"` removed')
# Remove `KALAMINE::BEPOLAR::BEGIN` & `KALAMINE::BEPOLAR::END` from fr file
path = "/usr/share/X11/xkb/symbols/"
 
with open(path+'fr','r') as file:
    lines = file.readlines()

with open(path+'fr','w') as file:
    for line in lines:
        x = re.findall("^// KALAMINE::", line)
        if not x:
            file.write(line)

print("`xkb/symbols/fr` file updated : `KALAMINE::` lines removed")