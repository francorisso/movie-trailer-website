#!/usr/bin/env bash

echo "Installing pip"
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
rm get-pip.py

echo "Installing Django"
sudo pip install django

echo "Installing rest_framework"
sudo pip install djangorestframework
sudo pip install markdown       # Markdown support for the browsable API.
sudo pip install django-filter  # Filtering support

echo "Installing setuptools"
sudo pip install setuptools

echo "Installing MySQL-python"
sudo pip install MySQL-python

echo "Installing Pillow"
sudo pip install Pillow

echo "Installing slugify"
sudo pip install slugify

echo "Installing requests"
sudo pip install requests