#!/usr/bin/bash

apt upgrade -y
apt install python
python3 -m pip install --upgrade pip
python3 -m pip install tqdm
python3 -m pip install pytube
python3 -m pip install pyfiglet
clear
python3 youtube.py
