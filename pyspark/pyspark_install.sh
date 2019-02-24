#!/usr/bin/bash

##########################
# pyspark ubuntu install #
##########################

sudo apt-get update
sudo apt-get install python3

#python add python alias
echo "# Add python alias" >> ~/.bashrc
echo "alias python=python" >> ~/.bashrc

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
sudo pip install pyspark
