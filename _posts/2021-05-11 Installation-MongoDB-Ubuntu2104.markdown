---
title: "Installation and Configuration of MongoDB in Ubuntu 21.04"
last_modified_at: 2021-05-10T17:20:00+01:00

categories:
  - Blog
tags:
  - linux
  - Ubuntu 21.04
  - NoSQL
  - MangoDB
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"

---

## MangoDB
The [document site](https://docs.mongodb.com/) of MongoDB. 



## Installation
The installation of MongoDB should be very smooth. The documentation from official website is very useful. Please note that MongoDB did not include Ubuntu 21.04 as supported OS. But we can use the its repo for Ubuntu 20.04. The following is the summary of installation steps. 

```bash
# Import the MongoDB public GPG key
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

# Create the /etc/apt/sources.list.d/mongodb-org-4.4.list file for Ubuntu 20.04 (Focal):
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# update and install
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

After the installation, you can check which version of MangoDB you are using:
```bash
$ mongo --version

# response
MongoDB shell version v4.4.6
Build Info: {
    "version": "4.4.6",
    "gitVersion": "72e66213c2c3eab37d9358d5e78ad7f5c1d0d0d7",
    "openSSLVersion": "OpenSSL 1.1.1j  16 Feb 2021",
    "modules": [],
    "allocator": "tcmalloc",
    "environment": {
        "distmod": "ubuntu2004",
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}
```

## Local Configuration
To use the MongoDB server, some local configurations are necessary. 
1. Create a local folder. This folder will be used by the MongoDB server to read and write data. Please note that this folder is located in Root. `-p` option makes it possible to create a folder even the mother folder does not exist. 
   ```bash
   $ sudo -p /data/db
   ```
2. Change the ownership of the folder
   ```bash
   $ sudo -p chown USER /data/db
   ```

## Start the local server
```bash
# start the mongod process
$ sudo systemctl start mongod

# verify if mongod started successful
$ sudo systemctl status mongod

# response
● mongod.service - MongoDB Database Server
     Loaded: loaded (/lib/systemd/system/mongod.service; disabled; vendor preset: enabled)
     Active: active (running) since Wed 2021-05-12 17:48:52 CEST; 9s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 190793 (mongod)
     Memory: 56.4M
     CGroup: /system.slice/mongod.service
             └─190793 /usr/bin/mongod --config /etc/mongod.conf
```
### autostart after reboot
```bash
$ sudo systemctl enable mongod
```
### Stop the server 
```bash
$ sudo systemctl stop mongod
```
### Restart the server 
```bash
$ sudo systemctl restart mongod
```

## Basic CURD with MongoDB
connect the the server 
```bash
$ mongo shell
>
```
### Add a DB and a collection
```mongo
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB

> use testDB
> db.products.insertOne({_id:1, name: "Pen", price: 1.1})
{ "acknowledged" : true, "insertedId" : 1 }

```

## MongoDB Drivers vs Mongoose
[MongoDB drivers](https://docs.mongodb.com/drivers/node/current/) is used to interact with other languages. This is the native support of MongoDB.
```bash
$ mkdir FruitProjects
$ touch app.js
$ npm init -y
$ npm install mongodb
```

Mongoose is on the other hand is a ODM (Object Modeling for node.js). It is much more elegant and easier to use. 
```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/test', {useNewUrlParser: true, useUnifiedTopology: true});

const Cat = mongoose.model('Cat', { name: String });

const kitty = new Cat({ name: 'Zildjian' });
kitty.save().then(() => console.log('meow'));
```