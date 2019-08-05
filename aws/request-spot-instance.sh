#!/usr/bin

SPECIFICATION="{
  \"ImageId\": \"ami-1a2b3c4d\",
  \"KeyName\": \"pikey\",
  \"SecurityGroupIds\": [ \"sg-1a2b3c4d\" ],
  \"InstanceType\": \"t2.micro\",
  \"Placement\": {
    \"AvailabilityZone\": \"eu-west-1a\"
  },
  \"IamInstanceProfile\": {
      \"Arn\": \"arn:aws:iam::123456789012:instance-profile/my-iam-role\"
  }
}"

CMD="aws ec2 request-spot-instances --dry-run --region=eu-west-1 --spot-price \"0.0128\" --instance-count 1 --type \"one-time\" --launch-specification $SPECIFICATION\n"
echo $CMD
