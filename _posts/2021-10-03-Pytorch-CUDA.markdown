---
title: "CUDA and Pytorch on Ubuntu 21.10"
last_modified_at: 2022-01-09T17:00:00-06:00

categories:
  - Blog
tags:
  - Python
  - Pytorch
  - CUDA
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

# CUDA Installation
The installation guide can be found [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/).Supported GPU is listed [here](https://developer.nvidia.com/cuda-gpus#compute).<br>
**NOTE:** In the official installation, the supported Ubuntu is 20.04. However, it seems the current version of CUDA (11.5.1) is compatible with Ubuntu 21.10. 

My PC and OS:
* Ubuntu 21.10
* GeForce GTX 1050

Check the version of Ubuntu
```console
yang@yzubuntu:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 21.10
Release:        21.10
Codename:       impish
```

Check the version of Linux Kernel.
```
yang@yzubuntu:~$ uname -r
5.13.0-23-generic
```

## check the GPU

```console
yang@yzubuntu:~$ lspci | grep -i nvidia
01:00.0 VGA compatible controller: NVIDIA Corporation GP107 [GeForce GTX 1050] (rev a1)
01:00.1 Audio device: NVIDIA Corporation GP107GL High Definition Audio Controller (rev a1)
```

## Pre-installation 
### gcc
```console
yang@yzubuntu:~$ gcc --version
gcc (Ubuntu 11.2.0-7ubuntu2) 11.2.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
### kernel headers and development packages
```console
yang@yzubuntu:~$ sudo apt-get install linux-headers-$(uname -r)
```

## Install
### Download the *.deb file and install
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.5.1/local_installers/cuda-repo-ubuntu2004-11-5-local_11.5.1-495.29.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-11-5-local_11.5.1-495.29.05-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu2004-11-5-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```
## Post-installation
The following steps must be done to make sure Ubuntu can find the location of `nvcc`
```console
yang@yzubuntu:~/Downloads$ echo 'export PATH=/usr/local/cuda-11.5/bin${PATH:+:${PATH}}' >> ~/.bashrc
yang@yzubuntu:~/Downloads$ echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.5/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
```
Check if the process is started. 
```console
yang@yzubuntu:~/Downloads$ systemctl status nvidia-persistenced
```

## Check CUDA version
```console
yang@yzubuntu:~/Downloads$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0
```

## CUDA Example
One example of using CUDA can be found [here](https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux).

## Wayland disappears after CUDA installation
By default, Ubuntu 21.10 uses wayland instead of X11. However, after CUDA installation, there is no option to choose wayland when logging into the system. This needs to be checked. 

# Pytorch
The official installation guide can be found [here](https://pytorch.org/get-started/locally/)<br>
**NOTE:** It seems Pytorch supports CUDA 11.1. My CUDA version is 11.4. The installation process did not result into error. But it needs further test with running projects. 
## Make a virtual environment
```console
yang@yzubuntu:~/Desktop/pytorch_test$ virtualenv --python=/usr/local/bin/python3.8 pytorch_test
created virtual environment CPython3.8.10.final.0-64 in 232ms
  creator CPython3Posix(dest=/home/yang/Desktop/pytorch_test/pytorch_test, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/yang/.local/share/virtualenv)
    added seed packages: pip==21.1.2, setuptools==57.0.0, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```
## Activate the virtual env
```console
yang@yzubuntu:~/Desktop/pytorch_test$ source pytorch_test/bin/activate
(pytorch_test) yang@yzubuntu:~/Desktop/pytorch_test$ pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
```
## Test the Installation
Create a file `test.py` and add the following.
```python
import torch
x = torch.rand(5, 3)
print(x)
```

```console
(pytorch_test) yang@yzubuntu:~/Desktop/pytorch_test$ python test.py 
tensor([[0.2932, 0.9057, 0.3990],
        [0.6864, 0.6373, 0.3777],
        [0.4606, 0.1394, 0.6477],
        [0.0674, 0.8054, 0.0522],
        [0.9636, 0.1747, 0.5445]])

```

## Check Pytorch Use CUDA 
Create a file `test2.py` and add the following.
```python
import os
import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))

```
