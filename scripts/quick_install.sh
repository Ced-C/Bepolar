#!/bin/bash

#####
# Deploy latest vertion of bepolar on Ubuntu and set it as default
#####

# Copy files in `xkb` directory for quick install
path=$(dirname "$0")

wget http://github.com/Ced-C/Bepolar/archive/master.tar.gz -O /dev/stdout -P $path | tar -zxf -
rsync -av $path/Bepolar-master/xkb/ ~/.config/xkb 
chown $USER:$USER -R ~/.config/xkb

# read -p 'Do you want to set up Bépolar as the default layout for the login screen (y/n) ' isDefault
# if [[ "$isDefault" == 'y' ]]
# then
# sudo sed -i "s/\(XKBVARIANT *= *\).*/\1\"bepolar\"/" /etc/default/keyboard
# sudo sed -i "s/\(XKBLAYOUT= *= *\).*/\1\"fr\"/" /etc/default/keyboard
# echo Bépolar set as default Keyboard layout
# fi
