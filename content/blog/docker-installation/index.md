---
title: "Install and use Docker on Ubuntu"
date: 2021-02-26
summary: "How to install Docker on Ubuntu and configure the Docker service."
categories:
  - Blog
tags:
  - linux
  - Ubuntu
  - Docker
---

# What is Docker

The official definition:

> Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.

## Docker architecture

This figure has illustrated the docker architecture very well. <br>
![docker](/images/docker_architecture.png)

# Installation

Follow the installation from the [official website](https://docs.docker.com/engine/install/ubuntu/). The [tutorial](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) from this page is also very helpful.

# How to start the docker service

I installed a docker add-on in my vs-code. However, it shows "Failed to connect. Is Docker running". I assume that I did not start the docker service. In the second tutorial, it specially mentioned that.

> The Docker service needs to be setup to run at startup.
> The tutorial suggets:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

I am not sure if these are needed. More investigations should be done. The vs code is because the docker daemon must has the sudo previlige, while vs code is only a normal user. To change this, need to add a usergroup and give the right from root to the user. I would not do it.
