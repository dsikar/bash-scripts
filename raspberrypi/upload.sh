#!/bin/bash

while [ true ]
do
  sudo raspistill -q 5 --nopreview --timeout 1 -o image.jpg -w 640 -h 480 -rot 180 -ifx sketch
  sftp -i ~/.ssh/pikey mailinfo@sikarsystems.com:public_html/images/ <<< $'put image.jpg'
  # sleep 1
done 
