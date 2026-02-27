---
title: "Python Configuration in Ubuntu 21.04 or 21.10"
date: 2021-05-01
summary: "Installing Python from source on Ubuntu 21.04/21.10, managing virtual environments, and troubleshooting common issues."
categories:
  - Blog
tags:
  - linux
  - Ubuntu 21.04
  - Ubuntu 21.10
  - Python
---

## Default python

```
python3 -V
```

In Ubuntu 21.04, the default Python installation are Python 3.9.4 and Python 2.7.18. They come with the Ubuntu installation and are located in `/usr/bin/python`. Because it usually requires special version of Python with different projects. It is always a good idea to install different versions of Python in the local.

## Normal installation with Ubuntu.

Normally, it is very easy to install in Ubuntu. Follow this excellent [page](https://medium.com/analytics-vidhya/how-to-install-and-switch-between-different-python-versions-in-ubuntu-16-04-dc1726796b9b) to do it. The method relies on a PPA `ppa:deadsnakes/ppa`. However, this PPA only support up to Ubuntu 20.10. Thus, we have to turn to install Python from resource. Here is a [page](https://brennan.io/2021/06/21/deadsnakes-hirsute/) that may work to use PPA on higher Ubuntu version. I have not tested it yet.

## Install python3.8 from Resource

1. Install required packages for Python. Some of the following packages might be missing and cannot be installed. Just delete the missing packages.
   ```console
   $ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev build-essential libreadline-dev libffi-dev zlib1g-dev liblzma-dev lzma
   ```
2. Download the \*.tgz from the [resource](https://www.python.org/downloads/source/).
3. Navigate to the downloaded place and use the following command to unzip the file. `tar xf Python-3.8.9.tgz`
4. Navigate to the unzipped folder by using `cd Python-3.8.9` and run the configuration file `./configure`
5. Use the following commands to install Python 3.8. Please make sure use `sudo make`. I have tried `make` and `sudo make install`. It turns out that Python3.8 can be installed but I cannot use pip after the installation. The error code is **pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.** I have no idea why it happens. I have tried to follow this [page](https://help.dreamhost.com/hc/en-us/articles/360001435926-Installing-OpenSSL-locally-under-your-username) to install a new **openssl** in `usr/local/bin`. But it does **NOT** help.
   ```console
   $ sudo make && sudo make install
   ```
6. Now python is installed in `usr/local/bin`. It will overwrite the default Python 3.9.4 and runs as default.
   ```
   $ python3 -V
   ```

## Package LZMA Missing

After installing from resource, it can have an error showing `ModuleNotFoundError: No module named '_lzma'`. This can be due to that the installation is from source and incomplete. To solve this problem, follow this [discussion](https://stackoverflow.com/questions/57743230/userwarning-could-not-import-the-lzma-module-your-installed-python-is-incomple). A complete solution is to install `liblzma-dev` and `lzma` using `sudo apt-get install`. Afterwards, re-install the python package. The complete code is as follows:

```console
$ sudo apt-get install liblzma-dev
$ sudo apt-get install lzma
$ tar xf Python-3.8.12.tgz
$ cd Python-3.8.12/
$ ./configure
$ sudo make && sudo make install
```

## Use Python built-in venv to manage virtual environments

### Use the default python

If using python3, will use the default python to create a virtual environment.

```console
$ python3 -m venv test_env
$ cd /test_env
$ source bin/activate
```

### Use another version of python

You can specify a specific version of python that you want to use in the virtual environment.

```console
$ python3.9 -m venv test_env2
$ cd /test_env2
$ source bin/activate
```

## Use Virtualenv to configure the virtual development environment.

```
$ mkdir test_py
$ cd test_py/
$ virtualenv --python=/usr/local/bin/python3.8 py_38_env
```

`py_38_env` is the virtual environment name. Use `source py_38_test/bin/activate` to activate the virtual environment. Use `deactivate` to exit the virtual environment.

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
