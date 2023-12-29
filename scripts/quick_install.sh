#!/bin/bash

#####
# Deploy latest vertion of bepolar on Ubuntu and set it as default, including at screen start 
#####

# Copy files in `xkb` directory for quick install
path_config=/usr/share/X11/xkb
path=$(dirname "$0")


sudo mv $path_config/rules/evdev.xml    $path_config/rules/evdev.xml.bk
sudo mv $path_config/rules/base.xml     $path_config/rules/base.xml.bk
sudo mv $path_config/symbols/fr         $path_config/symbols/fr.bk

sudo cp $path/../xkb/rules/evdev.xml    $path_config/rules/evdev.xml
sudo cp $path/../xkb/rules/base.xml     $path_config/rules/base.xml
sudo cp $path/../xkb/symbols/fr         $path_config/symbols/fr

read -p 'Do you want to set up Bépolar as the default layout for the login screen (y/n) ' isDefault
if [[ "$isDefault" == 'y' ]]
then
sudo sed -i "s/\(XKBVARIANT *= *\).*/\1\"bepolar\"/" /etc/default/keyboard
sudo sed -i "s/\(XKBLAYOUT= *= *\).*/\1\"fr\"/" /etc/default/keyboard
echo Bépolar set as default Keyboard layout
fi
