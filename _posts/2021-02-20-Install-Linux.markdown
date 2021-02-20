---
title: "Install Linux to PC and initial configuration"
last_modified_at: 2021-02-20T16:20:02-05:00

categories:
  - Blog
tags:
  - linux
  - Ubuntu
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

# Why Linux
I have encountered some problems on the Windows platform while I was learing the full-stack developer course. Thus I would like to give it a try on a linux environment. 

# My original PC
Hardware:
- i5-6600K
- Asus z170a motherboard
- 2*8G memory
- nvme SSD 256 G
- HHD 2TB

I have a duel system on the PC. However, I have not been using the ubuntu since installation. The partition of the harddrives is not clean. With years of using, too many softwares have been installed on this PC. Thus, I have decided to make a clean installation. 

# Clean format of the harddrive. 
I use a pre-made winPE usbdrive to boot the system and format both harddrives. The winPE is downloaed from[wepe](http://www.wepe.com.cn/). Use this  [tutorial](https://www.jianshu.com/p/50fd699ea916) to write the winPE into a usb drive. In general it is very simple. The winPE usb drive uses 'exFAT' format. <br>

# Download the latest ubuntu installatio file. 
Download the latest .iso file and use Rufus to write the iso file into a bootable usb drive. Please see this [video](https://www.youtube.com/watch?v=W-RFY4LQ6oE&t=605s). I used the default setting. 
 
# Boot from winPE and format the two harddrivers. 
The winPE system has a pre-installed software "Disk Genius". Use it to clean all the data from the harddrivers. Make sure to have already backed up all data. Because this will remove everything! 

# Insert the ubuntu usb drive and install.
Again, check the video. I installed Ubuntu in the SSD drive. The installation goes very smooth. There is no need to 

# How to Mount a Disk
I have a hdd drive of 2TB. Which is not yet mounted to the system. I cannot use it after loggning into the system. I follwed the [tutorial](https://askubuntu.com/questions/125257/how-do-i-add-an-additional-hard-drive) to mount the disk.  There are in general the following steps:
* install a partition tool
```bash
# install a partition tool garted
sudo apt-get install gparted

```
* use the partition tool to make partitions. Here I refered to this [tutorial](https://linuxhint.com/gparted_ubuntu/). One thing need to **NOTE**. After apply the changes, I found that the partition is automatically mounted to `/media/yang`, which I did not know why. But the gparted tool allow you to demount it. check the below example. <br>
![gparted](/assets/images/gparted.png)

* run the following commands
```bash
# check the available partitions
sudo fdisk -l
# make a mount point. /hdd is the mount point. Please note that this point is not under the user folder. 
sudo mkdir /hdd
```

* Edit /etc/fstab with `root` permission
```bash
sudo vim /etc/fstab
```

* Add the following line to the file
```
/dev/sda1    /hdd    ext4    defaults    0    0
```

* Mount the partition
``` sudo mount /hdd```

**Problem** After doing the above, I found myself that I have no permission to write in the mounting point. I guess it is because the current user has not been assigned the permission. Use the following commans to assign. 
```bash
sudo chown -R yang:yang /hdd
```

# How to install Chinese.
This is very simple. Just need to install `ibus`. Follow this [tutorial](https://askubuntu.com/questions/59356/how-do-i-get-chinese-input-to-work). 现在可以用拼音了。Jag har ocksä svenska i datorn.

# Install vscode.
**NOTE** Do not install vscode from ubuntus software center. It has problems with Chinese input. Download from official site and intall by `sudo apt install ./<file>.deb`

