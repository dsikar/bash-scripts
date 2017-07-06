#!/usr/bin

# TODO
# 1. Get wallet id from file

ALG=$1
FOUND=false
case $ALG in
    Script )
        echo "Using Script algorithm"
        FOUND=true
        ;;
esac

if $FOUND ; then
    echo "Algorithm found"
fi

