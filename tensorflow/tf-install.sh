#!/usr/bin

# update
sudo apt-get update
# from https://www.tensorflow.org/install/install_linux
sudo apt-get install libcupti-dev -y
# Installing with virtualenv using python 2.7 ~ run "python --version" to check
# 1. Install pip and virtualenv by issuing one of the following commands:
sudo apt-get install python-pip python-dev python-virtualenv # for Python 2.7
# 2. Create a virtualenv environment by issuing one of the following commands:
mkdir ~/tensorflow
virtualenv --system-site-packages ~/tensorflow # for Python 2.7
# 3. Activate the virtualenv environment by issuing
source ~/tensorflow/bin/activate
# 4. Issue one of the following commands to install TensorFlow in the active virtualenv environment: (pip required)
cd ~/tensorflow
pip install --upgrade tensorflow



