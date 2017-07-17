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
        PORT="3333"
        ;;
esac

case $ALG in
    sha256d )
        echo "Using SHA256 algorithm"
        FOUND=true
        PORT="3334"
        ;;
esac

case $ALG in
    scryptnf )
        echo "Using ScryptNf algorithm"
        FOUND=true
        PORT="3335"
        ;;
esac

case $ALG in
    x11 )
        echo "Using ScryptNf algorithm"
        FOUND=true
        PORT="3336"
        ;;
esac

case $ALG in
    x13 )
        echo "Using ScryptNf algorithm"
        FOUND=true
        PORT="3337"
        ;;
esac

case $ALG in
    keccak )
        echo "Using ScryptNf algorithm"
        FOUND=true
        PORT="3338"
        ;;
esac

case $ALG in
    x15 )
        echo "Using ScryptNf algorithm"
        FOUND=true
        PORT="3339"
        ;;
esac

case $ALG in
    nist5 )
        echo "Using ScryptNf algorithm"
        FOUND=true
        PORT="3340"
        ;;
esac

case $ALG in
    lyra2re )
        echo "Using Lyra2RE algorithm"
        FOUND=true
        PORT="3342"
        ;;
esac

if $FOUND ; then
    echo "Algorithm found"
    URL="stratum+tcp://$ALG.eu.nicehash.com:$PORT"

    CMD="./cpuminer --url=$URL --algo=$ALG --user=$WALLET"
    eval $CMD
fi

