---
title: "Use Scrcpy to Mirror Android Phone"
last_modified_at: 2021-03-08T09:20:00+01:00

categories:
  - Blog
tags:
  - linux
  - Ubuntu
  - Android
  - Phone Mirroring and Control
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

## What is SCRCPY
Today I found an very good package [SCRCPY](https://github.com/Genymobile/scrcpy). This great tool enables mirroring and control of an android device from Desktop. This package is available for Linux, Windows and Mac OS. It is completely free. This package is very helpful for people who would not like switching between devices. You can do everything just on the desktop! 
>This application provides display and control of Android devices connected on USB (or over TCP/IP). It does not require any root access. It works on GNU/Linux, Windows and macOS.

## Installation
1. Enable the USB debugging in the android device. I am using oneplue 7 pro. This can be done through the following steps.  About the phone >> click the "Version Nr" for several times. This will enable the developer mode. >> go to "system / developer options" and enable USB debugging. <br>

<img src="/assets/images/usb_debug.png" alt="usb_debug" width="400"/>

2. Install SCRCPY in the Linux PC. I am using the Ubuntu 20.04 and the default version of SCRCPY will be 1.12, which is a bit of out dated. New version of SCRCPY has many good features. In Ubuntu we can use [snap](https://snapcraft.io/scrcpy) to install the latest version of SCRCPY. Use the following commands to install. ```sudo snap install scrcpy```

## How to use it
1. use a usb cable to connect android phone with the PC. 
In bash terminal:
```bash
scrcpy
```
This will execute the Scrcpy server. A reminder will appear in the phone device. Allow it. 

2. Enjoy it. 

**NOTE** The above has an issue that when the screen goes off in phone, the screen will also go off in the PC. To avoid this, use the following command to start the SCRCPY server. `scrcpy -w -S`. <br>
* `-w` is equal as `--stay-awake`. To prevent the device to sleep. 
* `-S` is equal as `--turn-screen-off`. To turn the device off while mirroring on start. 

## Use it over Wifi
The connection via USB is the prerequisite for the connecting over wifi. To do so it is very simple. An introduction of using wifi is [here](https://www.genymotion.com/blog/open-source-project-scrcpy-now-works-wirelessly/).<br>
1. Find the phone ip address(internal address). This can be done through checking the router status, checking the status in phone, etc. 
2. Use the following commands in linux. The `192.168.1.248` should be replaced by your phone address. 
```bash
adb tcpip 5555
adb connect 192.168.1.248:5555
scrcpy -w -S
```
**BUG**: It seems that there is a bug when connected over wifi. The phone cannot be stayed awake. The screen will go off after a while. 
3. Enjoy.
4. To switch back to USB mode: `adb usb`
<img src="/assets/images/connection_over_wifi.png" alt="wifi_connection" width="400"/> <br>

## Transfer files 
* Scrcpy supports drag and copy from PC to phone. File will be located in /sdcards.
* Not sure if it support backwards copy from phone to PC. Here is a [topic](https://github.com/Genymobile/scrcpy/issues/1227) in Github. 
  
