#!/usr/bin

# Run tor via vpn on ubuntu

# update
sudo apt-get update
# move to home dir
cd ~/
# install vpn
sudo apt install openvpn easy-rsa
# install tor
sudo apt-get install tor
# get tor config file
wget https://www.ovpn.com/download/configurations/tor-ovpn.zip
# unpack
unzip tor-ovpn.zip
# save as config file
mv tor-ovpn.ovpn .torrc
# clean up
rm tor-ovpn.zip
# get browser - 32 bit version (in this case)
wget https://www.torproject.org/dist/torbrowser/7.5a1/tor-browser-linux64-7.5a1_en-US.tar.xz
tar -xvf tor-browser-linux64-7.5a1_en-US.tar.xz
# clean up
rm tor-browser-linux64-7.5a1_en-US.tar.xz
# launch browser (will launch firefor)
cd tor-browser_en-US/
./start-tor-browser.desktop
