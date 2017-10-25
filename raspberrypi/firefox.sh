#!/usr/bin

# Install Firefox on Pi Zero W as seen on https://www.raspberrypi.org/forums/viewtopic.php?t=150438

#  ### ###      #  ###     ### ###  #  ### 
#    # #       ##  # #       # # # ##    # 
#  ### ###      #  # #     ### # #  #    # 
#  #     #      #  # #     #   # #  #    # 
#  ### ###  #  ### ###  #  ### ### ###   # 

sudo apt install dirmngr

echo "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu trusty main" | sudo tee /etc/apt/sources.list.d/firefox.list
echo "deb-src http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu trusty main" | sudo tee /etc/apt/sources.list.d/firefox-source.list
echo "deb http://ppa.launchpad.net/mozillateam/thunderbird-next/ubuntu trusty main" | sudo tee /etc/apt/sources.list.d/thunderbird.list
echo "deb-src http://ppa.launchpad.net/mozillateam/thunderbird-next/ubuntu trusty main" | sudo tee /etc/apt/sources.list.d/thunderbird-source.list

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9BDB3D89CE49EC21
sudo apt update && sudo apt install firefox thunderbird
