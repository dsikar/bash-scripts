#!/usr/bin

# simplified miner - no safety nets!

ALG=$1
PORT=$2
WALLET=$(<~/.wallet)
URL="stratum+tcp://$ALG.eu.nicehash.com:$PORT"
CMD="./cpuminer --url=$URL --algo=$ALG --user=$WALLET"
eval $CMD

