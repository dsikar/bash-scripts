#!/usr/bin

# Install Firefox on Pi Zero W as seen on https://www.raspberrypi.org/forums/viewtopic.php?t=150438

#  ### ###      #  ###     ### ###  #  ### 
#    # #       ##  # #       # # # ##    # 
#  ### ###      #  # #     ### # #  #    # 
#  #     #      #  # #     #   # #  #    # 
#  ### ###  #  ### ###  #  ### ### ###   # 

echo 'deb http://q4os.org/qextrepo q4os-rpi-firefox-cn main' | sudo tee /etc/apt/sources.list.d/qextrepo.list
wget -nv -O- http://q4os.org/qextrepo/q4a-q4os.gpg.pub | sudo apt-key add -
sudo apt-get update
sudo apt-get install firefox
