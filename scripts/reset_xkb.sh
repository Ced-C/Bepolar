#!/bin/bash
# Restore original keyboard layout settings

path=/usr/share/X11/xkb

sudo cp $path/rules/evdev.xml.bk $path/rules/evdev.xml
sudo cp $path/rules/base.xml.bk $path/rules/base.xml
sudo cp $path/symbols/fr.bk $path/symbols/fr

echo "files restored to default value"