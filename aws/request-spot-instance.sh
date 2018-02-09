#!/usr/bin

# Launch AWS spot instance

aws ec2 request-spot-instances --instance-count 1 --spot-price "0.0128" --type "one-time" --launch-specification file://specification.json

