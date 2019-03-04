#!/usr/bin/bash

##########################
# pyspark ubuntu install #
##########################

# TODO JAVA INSTALL

# install python 3.6
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

# change symlink
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.6 /usr/bin/python
# this should now say python3.6
which python


# Yarn install from https://linuxize.com/post/how-to-install-yarn-on-ubuntu-18-04/
# yarn repo
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -

# Add Yarn APT repo
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

# install yarn
sudo apt update
sudo apt install yarn

# Check version
echo "Yarn version"
yarn --version

# install pip
sudo apt install python3-pip

# install pyspark
sudo pip3 install pyspark

# install jupyter notebook
sudo pip3 install jupyter


