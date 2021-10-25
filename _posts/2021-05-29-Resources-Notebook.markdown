---
title: "Notebook"
last_modified_at: 2021-05-29T18:20:00+01:00

categories:
  - Notebook
tags:
  - programming
  - notebook
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

## Python
### Callback functions
TBC

### Parameters in functions
TBC


## Pandas
### Round timestamp
```python
# round the timestamp to min
df_plc['Time'] = df_plc['Time'].apply(lambda x: x.round('min'))
```

### Timestamp resampling
Reference page is [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.resample.html).

```python
# upsample a time series dataset. It is like group. 
akeb_data = akeb_data.set_index('Time')
akeb_data_resample = akeb_data.resample('5T').ffill()
```

## matplotlib
### Add Chinese fonts in Matplotlib figures. 
When I use matplotlib to generate pictures in Ubuntu, it sometimes cannot display Chinese characters. The solution is the method in this [page](https://programming.vip/docs/how-to-make-matplotlib-display-chinese-smoothly-in-ubuntu-16.04.html). A short summary is below: 
* use the following commands to check the fonts folder.
  ```python
  import matplotlib
  matplotlib.matplotlib_fname()
  ```
  In my environment, it gives the following location ```/home/yang/Desktop/weight&food/weight/lib/python3.9/site-packages/matplotlib/mpl-data/matplotlibrc```. This is a configuration file located in my local python virtual environment. 
* navigate to the folder ```/home/yang/Desktop/weight&food/weight/lib/python3.9/   site-packages/matplotlib/mpl-data/fonts/ttf/``` and paste a new chinese font file `simhei.ttf` to the folder. The font file can be found [here](/assets/others/simhei.ttf).
* edit the `matplotlibrc` file.  
  * The line `#font.family: sans-serif` should be **uncommented** and changed to `font.family : sans-serif`
  * The line `#font.sans-serif` should also be **uncommented** and add the new font 'SimHei' to it. It should be look like the following. 
  ```
  font.family         : sans-serif
  font.sans-serif     : SimHei, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif

  ```
* Delete ~/.cache/matplotlib/
  ```bash
  cd ~/.cache/
  rm -rf matplotlib/
  ```
* restart the kernel
* when wanting to use Chinese font, using the following when drawing figures.
  ```python
  import matplotlib.pyplot as plt
  if ifChinese == True:
       plt.rcParams['font.family'] = 'SimHei'
  else:
       plt.rcParams['font.family'] = 'DejaVu Sans'
        
  ```
<div style="text-align: center"><img src="/assets/images/piechart_chinese.png" alt="food pie chart" width="800"/></div>

## VPN
The tool is in [Github](https://github.com/shadowsocks). Their website is [here](http://shadowsocks.org/). Use ```shadowsocks-libev```. This [tutorial](https://zh.codepre.com/how-to-24542.html) is very helpful.

### A VPS server
1. Step 1: Installation
    ```bash
    # install snap
    sudo dnf install -y epel-release
    sudo dnf update -y
    sudo dnf install -y snapd

    # enable snapd service
    sudo systemctl start snapd.service
    sudo systemctl enable snapd.service

    # install snap core
    sudo snap install core

    # install server side
    sudo snap install shadowsocks-libev

    # check info
    snap info shadowsocks-libev
    ```
2. Step 2: server configuration
   * Make a new configuration file ```touch /snap/bin/config.json```
   * Open the new file and fill in the following information
        ```json
        {
        "server":"0.0.0.0",
        "nameserver":"8.8.8.8",
        "server_port":8828,
        "local_port":1080,
        "password":"password",
        "method":"chacha20-ietf-poly1305",
        "timeout":600,
        "mode": "tcp_and_udp"
        }
        ```
    * In the VPS setting, allow the TCP and UTP traffic at port `8828` 
    * Navigate to `cd /snap/bin/` and it has the following files:
        ```
        config.json                   shadowsocks-libev.ss-redir
        newpid                        shadowsocks-libev.ss-server
        shadowsocks-libev.ss-local    shadowsocks-libev.ss-tunnel
        shadowsocks-libev.ss-manager  ss-server-pid
        ```
    * Can start the server with `shadowsocks-libev.ss-server -c config.json`. However this method we must keep the terminal open. Otherwise, the server will stop after we close the terminal
    * Use `netstat -lptn` to check the internet ports that are using. 
    * **NOTE** The `nameserver` setting is dependent on the location of the server and the purpose. For example, if the server is located in China, it is useless to set the name server as `8.8.8.8`, which is a Google DNS. Because the DNS server cannot be accessed anyway. In that case, it is better to set the `nameserver` as `114.114.114.114`, which is a Chinese domestic DNS server. 
3. Step 3: Use it as a service. 
    * Create a new file. `sudo touch /etc/systemd/system/shadowsocks-libev.service`
    * Open the file and fill in the following contents.
        ```
        [Unit]
          Description=Shadowsocks-Libev Server
          After=network-online.target
            
        [Service]
          Type=simple
          ExecStart=/usr/bin/snap run shadowsocks-libev.ss-server -c /snap/bin/config.json
          Restart=always
          RestartSec=2
            
        [Install]
        WantedBy=multi-user.target
        ```
    * Start the server as a service
        ```bash
        # start the service
        sudo systemctl start shadowsocks-libev.service
        # enable auto start after rebooting
        sudo systemctl enable shadowsocks-libev.service
        # check the service
        systemctl status shadowsocks-libev.service
        ```

### Install a client on an android phone. 
Can either download from google play store or github release. Go in and make the configuration

### Install a client on an android TV.
I have a android TV (Xiaomi Stick). It comes with Google play. 

1. Install the following apps from google play. 
   * X-plore File Manger. (To open json files, which will be used in vps client).
   * Send files to TV. (Install both on mobile and android TV. To transfer files between mobile and android TV).
2. Export the configuration file from phone client. It is named as `profiles.json`. 
3. Download the following apk files.
   *  极光TV [link](https://tv.qq.com/)
   *  奇异果TV [link](https://app.iqiyi.com/tv/player/)
   *  Shadowsocks android client [link](https://github.com/shadowsocks/shadowsocks-android/releases/download/v5.2.4/shadowsocks-tv-google--universal-5.2.4.apk)
4. Transfer the `profiles.json` file and the apk files to TV through `Send files to TV`
5. Install the apk files. 
6. Open Shadowsocks client and choose `replace from files` and find the 'profiles.json' file. Then the server, port, and password will be updated.
7. Enjoy the TV side. 

### Use the service from a linux machine. 
* install shadowsocks-libev on a local machine
* use `shadowsocks-libev.ss-local` as the local client. Also need to make a configuration file. Check the following example. `sudo touch /var/snap/shadowsocks-libev/common/client-config.json`
  ```
  {
    "server":"SERVER IP ADDRESS",
    "mode":"tcp_and_udp",
    "server_port":8828,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"password",
    "timeout":60,
    "name_server":"8.8.8.8",
    "method":"chacha20-ietf-poly1305"
  }
  ```  
* navigate to `cd /snap/bin/`
* use `shadowsocks-libev.ss-local -c /var/snap/shadowsocks-libev/common/client-config.json` to start the local client connection. **NOTE** Have tried to build the the json file `/snap/bin/client-config.json`. It comes with error **Invalid config path**. Not clear why. But might be problems of snap links. The folder `/snap/bin/` looks kind of special. 
* need to configure proxy for the application that we want to use. For example firefox

<div style="text-align: center"><img src="/assets/images/firefox_proxy.png" alt="food pie chart" width="600"/></div>
<div style="text-align: center"><img src="/assets/images/firefox_ip.png" alt="food pie chart" width="600"/></div>

### OpenWrt on Raspberry pi
OpenWrt is an open-source project for embedded operating system based on Linux. OpenWrt can be used as a Router system. Simply download the Firmware and burn it in a SD card. Raspberry pi can then boot and run OpenWrt. It has many functions.

#### Download firmware and burn it into SD card. 
First check the version of Raspberry pi and different version of firmware at this [link](https://mlapp.cn/1004.html).
* Download the firmware from this [Github repo](https://github.com/SuLingGG/OpenWrt-Rpi). Please note that there are two types of file system (ext4 and quashfs). I used ext4 because this can be easily managed by Gparted. Please check the summry on this [page](https://mlapp.cn/1004.html).
* Use **Etcher** to burn the downloaded firmware into SD card. 
* The default partition is very little, which cannot make full use of the SD card. Use this [link](https://mlapp.cn/1011.html) to enlarge the size of the partition. It is very easy with Gparted on Linux system.
* Insert the SD card and boot. 

#### RPi Configuration
* The initial IP address of the OpenWrt will be `192.168.1.1`. This address needs to be revised before we can connect the RPi into our local network. This can be done by assigning a static IP to local computer. For example IP `192.168.1.117` and sub mask `255.255.255.0`. Connect the local PC with RPI and use browser to log into `192.168.1.1`. 
* A password will be need. The default setting is `password`. 
* Once logged into the OpenWrt system, we can revise the settings of the 'LAN' port. Assign a new static IP address to avoid collision with Router. The gateway of RPi should be the address of main router. In this case, it will be `192.168.1.1`. **Uncheck** the DHCP service in OpenWRT. Then Save and Exit.
* Unplug the RPi from PC and connect directly to Router. 
* Now the RPi can be accessed from any device in the same local network. 
<div style="text-align: center"><img src="/assets/images/lan_setup.png" alt="rpi lan setup" width="600"/></div>

#### A problem about firmware
I have two RPi. One model 2b and one model 4. On model 2b I installed "openwrt-bcm27xx-bcm2709-rpi-2-ext4-factory.img.gz" and on model 4 I installed "openwrt-bcm27xx-bcm2711-rpi-4-squashfs-factory". They differ in the file system. However, I found that it is very difficult to save configurations in Model 4 with the 'squashfs'. It is almost impossible to save configurations. Not sure why. Will test the ext4. 
<br>
The same problem reoccurs after a accident shutdown of rpi4. When using SSH to log in, it is noticed that we cannot make any changes to the files. It comes with the error `read only file system`. This happens to be a known problem, which is discussed [here](https://issueexplorer.com/issue/SuLingGG/OpenWrt-Rpi/155). The authors of the rpi firmware gives a [solution](https://openwrt.cc/restore/). As far as I understand, this problem is caused by the SD card. The previous file installations still remain in the sd card. There is not a 100% formatting. The author proposed to rewrite the SD card by a blank image and then reburn the openwrt firmware. The problem is solved after doing so. For the sake of future use, I copied the blank image, and you can find it [here](/assets/others/Restore-SDCard-4G.img.zip).

#### RPi wifi setup
Follow the example given in the following picture. Be careful with banwidth as well as the location. The wifi might function not well if changing. 
<div style="text-align: center"><img src="/assets/images/wifi_setup.png" alt="rpi wifi setup" width="600"/></div>
External wifi adapters did not function well due to lack of proper driver. This [youtube video](https://www.youtube.com/watch?v=h_m7mU2LYH4&t=326s) recommends one usb wifi adapter on Nano RS. 

#### Configure the SS using SSR+ service. 
Follow the following pictures. Add the server first. 
<div style="text-align: center"><img src="/assets/images/SSR_setup1.png" alt="rpi SSR setup" width="600"/></div>
<div style="text-align: center"><img src="/assets/images/SSR_setup2.png" alt="rpi SSR setup" width="600"/></div>
<div style="text-align: center"><img src="/assets/images/SSR_setup3.png" alt="rpi SSR setup" width="600"/></div>
<div style="text-align: center"><img src="/assets/images/SSR_setup4.png" alt="rpi SSR setup" width="600"/></div>

#### Use the rpi to re-route traffic in other devices. 
Let us assume rpi openwrt has the following IP address: 192.168.1.118
* Address: assign a IP address, for example 192.168.1.11
* Netmask: 255.255.255.0
* Gateway: 192.168.1.118
* DNS: 8.8.8.8

