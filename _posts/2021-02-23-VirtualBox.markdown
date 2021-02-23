---
title: "Virtual box cannot load GUI with Ubuntu"
last_modified_at: 2021-02-23T09:20:00+01:00

categories:
  - Blog
tags:
  - linux
  - Ubuntu
  - Virtual Box
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

# Vitual Box
>VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. 

It is a very powerful tool for a linux user to be able to use some programs that are not compatible with linux system. 
# Installation
There are various ways of installation. 
* Download directly from [official website](https://www.virtualbox.org/wiki/Linux_Downloads) and install via `sudo apt install ./xxx.deb`
* Use Ubuntu's software manager to install. This is the easiest way to install. However, you might not install the newest version. 
* The third way is to connect to Virtualbox's warehouse. In this way, you always get the newest version and can update through `sudo apt upgrade` <br>

This [tutorial](https://zhuanlan.zhihu.com/p/80527572) showes exactly how to install virtual box. 
**NOTE** Please also install the extensions. 

# Vitual box not compatible with Ubuntu Fractional Scaling
I am using Ubuntu 20.02 LTS. I have two monitors (2k and 4K resolution). I have been using the Fractional Scaling. <br>

![Fractional_scaling](/assets/images/ubuntu_fractional_scaling.png)
<br>

After installtion of VirtualBox, I cannot open it. Once opened, it only shows a box, no buttons or icons were shown. It simpliy shows the following picture. No error or hints were given. <br>

![Problem_virtualbox](/assets/images/virtualboxproblem.jpg)

# Solution
The solution is very simple. Just turn off fractional scaling. Now you can open virtualbox. The fractional scaling also have effects on Spotify. 

# Install host OS in Virtual Box. 
This can be done by refering to this [video](https://www.youtube.com/watch?v=OWmD8obq4eQ)