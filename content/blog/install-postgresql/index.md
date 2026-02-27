---
title: "Installation and Configuration of PostgreSQL in Ubuntu 21.04"
date: 2021-05-10
summary: "Step-by-step guide to installing PostgreSQL and pgAdmin4 on Ubuntu 21.04."
categories:
  - Blog
tags:
  - linux
  - Ubuntu 21.04
  - SQL
  - PostgreSQL
---

## Installation

The installation is very easy. Just follow the instructions in this [page](https://www.postgresql.org/download/linux/ubuntu/). The main steps are:

```bash
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
sudo apt-get -y install postgresql
```

## Check if postgreSQL server is running

```bash
$ sudo systemctl is-active postgresql
$ sudo systemctl is-enabled postgresql
$ sudo systemctl status postgresql
```

Giving the following response

```
● postgresql.service - PostgreSQL RDBMS
     Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
     Active: active (exited) since Mon 2021-05-10 20:13:16 CEST; 22min ago
    Process: 3235 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
   Main PID: 3235 (code=exited, status=0/SUCCESS)

May 10 20:13:16 yzubuntu systemd[1]: Starting PostgreSQL RDBMS...
May 10 20:13:16 yzubuntu systemd[1]: Finished PostgreSQL RDBMS.

```

This [page](https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu/) is useful.

## Create a database

Refer to this [page](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart) to learn how to create a database. By default installation, a new user 'postgres' will be added. We need to switch the our role to that account.

```bash
# Switch to postgres
$ sudo -i -u postgres

# We can create a database here
postgres@yzubuntu:~$ createdb testdb

# Connect to the PostgreSQL promts
postgres@yzubuntu:~$ psql

# Check the current databases
postgres=# \l

```

## Install pgadmin4

pgadmin4 is a GUI interface to help manage databases.

### Trying install both desktop and web from APT.

I have tried install both the desktop and web version. The installation guide is given [here](https://www.pgadmin.org/download/pgadmin-4-apt/). However, I have met various problems after installation. The last step `sudo /usr/pgadmin4/bin/setup-web.sh` always gives errors.

1. The first error message is below:

   ```bash
   Setting up pgAdmin 4 in web mode on a Debian based platform...
   Creating configuration database...
   /usr/pgadmin4/bin/setup-web.sh: line 64: /usr/pgadmin4/venv/bin/python3: No such file or directory
   Error setting up server mode. Please examine the output above.
   ```

   This error seems easy to fix. Use the method in this [link](https://www.scivision.dev/repairing-broken-symbolic-link-linux/) to fix the broken link.

   ```bash
   cd /usr/pgadmin4/venv/bin/
   readlink -v python3
   sudo ln -sfn /usr/local/bin/python3 python3
   ```

2. Second try <br>
   The second message is about Python libraries. pgadmin4 requires many python libraries to run. I tried to install with `pip3`. However, because I am using a local python, which is `/usr/local/bin/python3`. The installed libraries by `pip3` all went to a local place `~/.local` because of **Defaulting to user installation because normal site-packages is not writeable**. The pdadmin cannot configure because it cannot successfully import packages.
3. Third try
   Afterwards, I have tried to create a virtual environment. But it did not succeed because of `No module named '_ctypes'`. Possible solutions are `sudo apt-get install libffi-dev` and **re-install** python. But I did not try and gave up the installation.

### Install just the web version of pgadmin4.

The official [tutorial](https://www.pgadmin.org/download/pgadmin-4-python/) is very clear. I copied the main steps here.

```bash
# necessary preparation before installation. These folders should be created before installation. Otherwise, there will be permission issues to run as a normal user.
$ sudo mkdir /var/lib/pgadmin
$ sudo mkdir /var/log/pgadmin
$ sudo chown USER /var/lib/pgadmin
$ sudo chown USER /var/log/pgadmin

# Create a virtual environment
mkdir ~/Desktop/pgadmin_env
cd ~/Desktop/pgadmin_env
virtualenv --python=/usr/local/bin/python3.8 pgadmin_env
source pgadmin_env/bin/activate

# installation
pip3 install pgadmin4

# Run pgadmin
pgadmin4
```

### Enjoy it!

<div style="text-align: center"><img src="/images/pgadmin4.png" alt="usb_debug" width="800"/></div>
