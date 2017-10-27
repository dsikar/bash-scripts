#!/bin/bash

while [ true ]
do
  sudo raspistill -o image.jpg -w 640 -h 480 -rot 180 -ifx sketch
  scp -i ~/.ssh/pikey image.jpg  mailinfo@sikarsystems.com:~/public_html/images
  sleep 1
done 
