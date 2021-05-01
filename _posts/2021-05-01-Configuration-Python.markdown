---
title: "Python Configuration in Ubuntu 21.04"
last_modified_at: 2021-05-01T17:20:00+01:00

categories:
  - Blog
tags:
  - linux
  - Ubuntu 21.04
  - Python
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

## Default python
```
python3 -V
```
In Ubuntu 21.04, the default Python installation are Python 3.9.4 and Python 2.7.18. They come with the Ubuntu installation and are located in `/usr/bin/python`. Because it usually requires special version of Python with different projects. It is always a good idea to install different versions of Python in the local. 

## Normal installation with Ubuntu. 
Normally, it is very easy to install in Ubuntu. Follow this excellent [page](https://medium.com/analytics-vidhya/how-to-install-and-switch-between-different-python-versions-in-ubuntu-16-04-dc1726796b9b) to do it. The method relies on a PPA `ppa:deadsnakes/ppa`. However, this PPA only support up to Ubuntu 20.10. Thus, we have to turn to install Python from rescource. 

## Install python3.8 from Resource
1. Install required packages for Python. Some of the following packages might be missing and cannot be installed. Just delete the missing packages. 
   ```bash
   sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
   ```
2. Download the *.tgz from the [resource](https://www.python.org/downloads/source/). 
3. Navigate to the downloaded place and use the following command to unzip the file. `tar xf Python-3.8.9.tgz`
4. Navigate to the unzipped folder by using `cd Python-3.8.9` and run the configuration file `./configure`
5. Use the following commands to install Python 3.8. Please make sure use `sudo make`. I have tried `make` and `sudo make install`. It turns out that Python3.8 can be installed but I cannot use pip after the installation. The error code is **pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.** I have no idea why it happens. I have tried to follow this [page](https://help.dreamhost.com/hc/en-us/articles/360001435926-Installing-OpenSSL-locally-under-your-username) to install a new **openssl** in `usr/local/bin`. But it does **NOT** help. 
   ```bash
   sudo make && sudo make install
   ```
6. Now python is installed in `usr/local/bin`. It will overwrite the default Python 3.9.4 and runs as default. 
   ```bash
   python3 -V
   ```

## Use Virtualenv to configure the virtual development environment. 
```
virtualenv --python=/usr/local/bin/python3.8 py_37
```
`py_37` is the virtual environment name. 


## Useful links
The following links are useful. 
1. Tutorial about how to install a package from resource. [link](https://passingcuriosity.com/2015/installing-python-from-source/).
2. Solving the pip problem. [link](https://askubuntu.com/questions/1164352/cannot-use-pip-ubuntu-pip-is-configured-with-locations-that-require-tls-ssl)

## Remove the installation files from download
```bash
cd ~/Downloads/
rm Python-3.8.9.tgz
sudo rm -r Python-3.8.9
```
