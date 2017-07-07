#!/usr/bin

# TODO
# 1. Add URLs

echo "Reading walled id..."
while read p; do
    echo $p
done < ~/.wallet

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

