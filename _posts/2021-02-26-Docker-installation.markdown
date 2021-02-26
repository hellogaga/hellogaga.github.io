---
title: "Install and use Docker on Ubuntu"
last_modified_at: 2021-02-26T21:20:00+01:00

categories:
  - Blog
tags:
  - linux
  - Ubuntu
  - Docker
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

# What is Docker
The official definition:
>Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. 

# Installation
Follow the installation from the [official website](https://docs.docker.com/engine/install/ubuntu/). The [tutorial](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) from this page is also very helpful. 

# How to start the docker service 
I installed a docker add-on in my vs-code. However, it shows "Failed to connect. Is Docker running". I assume that I did not start the docker service. In the second tutorial, it specially mentioned that.
>The Docker service needs to be setup to run at startup.
The tutorial suggets:
```bash
sudo systemctl start docker
sudo systemctl enable docker
```
I am not sure if these are needed. More investigations should be done. 
