# 1. Run Blender instance (Dublin)
$ aws ec2 run-instances --image-id
          ami-23b48854 --count 1 --instance-type p2.xlarge --key-name MyKeyPair --security-group-ids sg-xxxxxxxx
# 2. SSH
$ ssh -i myprivatekey ubuntu@<public ip>

# 2.1 Configure GPU ~ http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/optimize_gpu.html
$ sudo nvidia-smi -pm 1
$ sudo nvidia-smi --auto-boost-default=0
$ sudo nvidia-smi -ac 2505,875

# 3. Download example
$ wget https://download.blender.org/demo/test/splash_fishy_cat_2.zip

# 4. Unzip
$ unzip splash_fishy_cat_2.zip

# 5. Change directory
$ cd blender_splash_fishy_cat

# 6. Create output directory
$ mkdir output

# 7. Render
$ blender -b fishy_cat.blend -x 1 -o /output -a

# Assemble *png output with any available tool
# Windows example using VirtualDub
# 1. File > Open
# 2. Video > Frame Rate
# 3. File > Save as AVI

