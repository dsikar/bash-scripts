#!/bin/bash

# start - to stop delete /tmp/runpiwebcam

STARTFILE="/tmp/runpiwebcam"

if [ ! -f $STARTFILE ]; then
  touch $STARTFILE
  echo "To stop webcam delete $STARTFILE"
fi

while [ true ]
do
  if [ -f $STARTFILE ]; then
    sudo raspistill -q 3 --nopreview --timeout 1 -o image.jpg -w 640 -h 480 -rot 180 -ifx sketch 
    sftp -i ~/.ssh/pikey mailinfo@sikarsystems.com:public_html/images/ <<< $'put image.jpg' 
    sleep 5
  fi
done 
