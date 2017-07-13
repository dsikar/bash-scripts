#!/usr/bin

# Crypto currency cpu mining courtesy of nicehash.com

# update
sudo apt-get update
# tools
sudo apt-get install build-essential libcurl4-openssl-dev git automake libtool libjansson* libncurses5-dev libssl-dev
# more tools
git clone --recursive https://github.com/tpruvot/cpuminer-multi.git
# get onto correct branch
cd cpuminer-multi
git checkout linux
# build
./autogen.sh
./configure CFLAGS="-march=native" --with-crypto --with-curl
make
# create a wallet, choose an algorithm and corresponding url, get mining e.g.
# WALLET=37H45eCwjADw5NDhoSttJ2XJUgPotepiwY
# ./cpuminer --url=stratum+tcp://lyra2re.eu.nicehash.com:3342 --algo=lyra2re --user=$WALLET
# see mine.sh
