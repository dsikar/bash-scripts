#!/usr/bin

# TODO
# 1. Add URLs

echo "Reading walled id..."
while read l; do
    WALLET=$l
done < ~/.wallet

ALG=$1
FOUND=false
case $ALG in
    scrypt )
        echo "Using Script algorithm"
        FOUND=true
        URL="stratum+tcp://scrypt.eu.nicehash.com:3333"
        ;;
esac

case $ALG in
    sha256 )
        echo "Using SHA256 algorithm"
        FOUND=true
        URL="stratum+tcp://sha256.eu.nicehash.com:3334"
        ;;
esac

if $FOUND ; then
    echo "Algorithm found"
    CMD="./cpuminer --url=$URL --user=$WALLET"
    eval $CMD
fi

