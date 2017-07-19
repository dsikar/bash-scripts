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
# Extra - download custom wheel
wget https://github.com/lakshayg/tensorflow-build/raw/master/tensorflow-1.2.1-cp27-cp27mu-linux_x86_64.whl
# Extra custom install in lieu of
# pip install --upgrade tensorflow
pip install --ignore-installed --upgrade tensorflow-1.2.1-cp27-cp27mu-linux_x86_64.whl



