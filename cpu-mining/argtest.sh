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
    Scrypt )
        echo "Using Script algorithm"
        FOUND=true
        URL="stratum+tcp://scrypt.eu.nicehash.com:3333"
        ;;
esac

if $FOUND ; then
    echo "Algorithm found"
    CMD="./cpuminer --url=$URL --algo=$ALG --user=$WALLET"
    eval $CMD
fi

