#!/bin/bash
# file to install Bépolar for my local config
# including the position bug related to Ubuntu/Gnome

path=$(dirname "$0")
$path/reset_xkb.sh

sudo xkalamine install Bépolar.yml
sudo xkalamine install Bépolar2.yml

sudo python3 $path/kalamine_clean.py

