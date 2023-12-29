#!/bin/bash
# file to install Bépolar for my local config
# including the position bug related to Ubuntu/Gnome
# usefull for deploying new version of Bépolar

path=$(dirname "$0")


# Compile lastest vertion and install
xkalamine install Bépolar.yml

# make version for ditribution `dist` directory
kalamine $path/../Bépolar.yml

# Save user-space for quick install
rsync -av ~/.config/xkb $path/../xkb/

# Get latest SVGs
python3 $path/generate_svg.py

