---
title: "Install Linux to PC and initial configuration"
date: 2021-02-20
summary: "Complete guide to installing Ubuntu Linux on a PC, including disk setup, software installation, and Python configuration."
categories:
  - Blog
tags:
  - linux
  - Ubuntu
---

## Why Linux

I have encountered some problems on the Windows platform while I was learing the full-stack developer course. Thus I would like to give it a try on a linux environment.

## My original PC

Hardware:

- i5-6600K
- Asus z170a motherboard
- 2\*8G memory
- nvme SSD 256 G
- HHD 2TB

I have a duel system on the PC. However, I have not been using the ubuntu since installation. The partition of the harddrives is not clean. With years of using, too many softwares have been installed on this PC. Thus, I have decided to make a clean installation.

## Clean format of the harddrive.

I use a pre-made winPE usbdrive to boot the system and format both harddrives. The winPE is downloaed from[wepe](http://www.wepe.com.cn/). Use this [tutorial](https://www.jianshu.com/p/50fd699ea916) to write the winPE into a usb drive. In general it is very simple. The winPE usb drive uses 'exFAT' format. <br>

## Download the latest ubuntu installatio file.

Download the latest .iso file and use Rufus to write the iso file into a bootable usb drive. Please see this [video](https://www.youtube.com/watch?v=W-RFY4LQ6oE&t=605s). I used the default setting.

## Boot from winPE and format the two harddrivers.

The winPE system has a pre-installed software "Disk Genius". Use it to clean all the data from the harddrivers. Make sure to have already backed up all data. Because this will remove everything!

## Insert the ubuntu usb drive and install.

Again, check the video. I installed Ubuntu in the SSD drive. The installation goes very smooth. There is no need to

## How to Mount a Disk

I have a hdd drive of 2TB. Which is not yet mounted to the system. I cannot use it after loggning into the system. I follwed the [tutorial](https://askubuntu.com/questions/125257/how-do-i-add-an-additional-hard-drive) to mount the disk. There are in general the following steps:

1. install a partition tool

```bash
sudo apt-get install gparted
```

2. use the partition tool to make partitions. Here I refered to this [tutorial](https://linuxhint.com/gparted_ubuntu/). One thing need to **NOTE**. After apply the changes, I found that the partition is automatically mounted to `/media/yang`, which I did not know why. But the gparted tool allow you to demount it. check the below example. <br>
   ![gparted](/images/gparted.png)

3. run the following commands

```bash
# check the available partitions
sudo fdisk -l
# make a mount point. /hdd is the mount point. Please note that this point is not under the user folder.
sudo mkdir /hdd
```

4. Edit /etc/fstab with `root` permission

```bash
sudo vim /etc/fstab
```

5. Add the following line to the file

```
/dev/sda1    /hdd    ext4    defaults    0    0
```

6. Mount the partition <br>
   ` sudo mount /hdd`

**Problem** After doing the above, I found myself that I have no permission to write in the mounting point. I guess it is because the current user has not been assigned the permission. Use the following commans to assign.

```bash
sudo chown -R yang:yang /hdd
```

## After Installation

### Install Chinese Input.

This is very simple. Just need to install `ibus`. Follow this [tutorial](https://askubuntu.com/questions/59356/how-do-i-get-chinese-input-to-work). 现在可以用拼音了。Jag har ocksä svenska i datorn.

### Install vscode.

**NOTE** Do not install vscode from ubuntus software center. It has problems with Chinese input. Download from official site and intall by `sudo apt install ./<file>.deb`

### WPS office very slow opening after install 'ibus'

Solution comes from this [page](https://blog.csdn.net/weixin_42751951/article/details/105919949).

```
sudo apt-get install libcanberra-gtk-module
sudo apt-get install appmenu-gtk2-module
```

This problem seems solved in the latest WPS version (Version 11.1.0.10702)

### Install flameshot to take screenshots

```console
$ sudo apt install flameshot
```

### Install missing fonts.

Some fonts are missing after the installation. For example, when using WPS, I get the following warning:<br>
<img src="/images/missing_fonts_wps.png" alt="missing_fonts_ubuntu"/>
<br>
Some missing fonts can be downloaded from this [website](https://www.wfonts.com/). Other missing fonts can be directly copied from a Windows Machine. In windows, the fonts can be found `C:\Windows\Fonts`. Copy the needed fonts to Ubuntu. And use the following commands to make the fonts available to all users of the machine.

#### True Type Fonts (TTF)

```console
$ sudo cp *.ttf *.TTF /usr/share/fonts/truetype/
$ sudo cp *.ttc /usr/share/fonts/truetype/
```

#### Open Type Fonts (OTF)

```console
$ sudo cp *.otf *.OTF /usr/share/fonts/opentype
```

### USB-Wifi adapter

1. Check the model of the wifi adapter

```console
$ lsusb
Bus 001 Device 004: ID 0bda:c811 Realtek Semiconductor Corp. 802.11ac NIC
```

2. Download and install the driver, check this [discussion](https://askubuntu.com/questions/1162974/wireless-usb-adapter-0bdac811-realtek-semiconductor-corp). The driver repo is [here](https://github.com/brektrou/rtl8821CU)

```console
$ cd ~/Downloads/
$ git clone https://github.com/brektrou/rtl8821CU.git
$ cd rtl8821CU/
$ sudo ./dkms-install.sh
```

3. Reboot the PC. Now you can see the WIFI.

### Gnome extensions

Install the chrome extension for gnome. Install through `sudo apt install chrome-gnome-shell`. After installation, go to the gnome [page](https://extensions.gnome.org/) to install extensions for gnome. I used to install the following extensions.

1. OpenWeather
2. Simple System Monitor
3. Application Menu

### Enabling SSH on Ubuntu

This is quite straight-forward. Install the openssh server and start the service.

```console
$ sudo apt install openssh-server
$ sudo systemctl status ssh
```

## Install python on LTS ubuntu

Check this [tutorial](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/). The following tutorial is for the LTS version of Ubuntu. For Ubuntu verison other than the LTS, please refer to "Python Configuration in Ubuntu 21.04 or 21.10".

### A specific version of Python

Ubuntu comes with python installed. However, you can install another verison of python
check this [page](https://medium.com/analytics-vidhya/how-to-install-and-switch-between-different-python-versions-in-ubuntu-16-04-dc1726796b9b). It is about how to install different version of python and switch between them.
This [page](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) is also about how to install a different version.

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7

```

Next, go to the virtualenv section to specify the python version.

### install pip

```
sudo apt-get install python3-pip
pip3 --version
```

### Install virtualenv

```
sudo pip3 install virtualenv
virtualenv --version
```

### How to use virtualenv

- make a project folder using `mkdir pythontest`. Navigate to the project folder by `cd pythontest`
- run `virtualenv py_env`. `py_env` is the virtual environment name.
- run `source py_env/bin/activate` to activate the virtual environment.
- use `pip` or `pip3` to install required packages.
- run `deactivate` to deactivate from the virtual environment.

#### Build a virtualenv with specific python version

```
virtualenv --python=/usr/bin/python3.7 py_37
```

'py_37' is the virtual environment name. This should be done when the system has a python 3.7 installed. Reference is [here](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv/39713544#39713544).

#### How to delete the virtualenv

Just delete the `py_env` folder.
