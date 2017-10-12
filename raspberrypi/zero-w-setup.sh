# Setting up the Raspberry Pi Zero W v1.1

# SD Card preparation
# 1. SD Card - Sandisk 16GB Ultra Micro SD SDHC Memory Card 48MB/s UHS-I Class 10
# http://www.ebay.co.uk/itm/202013230777
# 2. Image - "RASPBIAN STRETCH WITH DESKTOP" https://downloads.raspberrypi.org/raspbian_latest
# 3. Imager - Win32 Disk Imager https://sourceforge.net/projects/win32diskimager/

# Internet connection setup via desktop

# Update & upgrade
sudo apt-get update && sudo apt-get upgrade

# Install apache2
sudo apt-get install apache2 

# Enable ssh - run
sudo raspi-config
# then option 5 Interfacing Options, then P2 SSH Enable

# Setting up a static ip address

