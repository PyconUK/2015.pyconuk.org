type: session
title: "The fabric that holds the cloud together: use Python fabric library to manage your OpenStack environment"
slug: "the-fabric-that-holds-the-cloud-together-use-python-fabric-library-to-manage-your-openstack-environment"
url: "talks/the-fabric-that-holds-the-cloud-together-use-python-fabric-library-to-manage-your-openstack-environment/index.html"
body_class_hack: talks
---

### Konstantin Benz

What's this session about?
Fabric is a Python library that offers a simple API to manage remote connections to distant servers and PCs via SSH protocol. Although it is a simple library, fabric is an extremely powerful tool for managing virtual machines in the cloud. Fabric can be used to login to virtual machines, upload files to them, install software packages on them or download files of them. Furthermore fabric can be extended to a fully-fledged (but still lightweight) configuration management tool. Fabric can be combined with the Python cuisine library and Python's "native" capabilities like serializing objects, writing data to JSON files and manipulating regular expressions. By employing this capabilities almost every VM administration task can be automated. VMs can be connected to each other, they can authenticate with each other and they can communicate to each other. In short: fabric is the "glue" that holds your VM environment together. If you're involved into DevOps, fabric is your tool to manage the cloud. You will get to know to do this in this session.

Overview
In this talk we will show you fabric's capability to manage and configure virtual machines in the popular Python-based cloud operating system OpenStack. Thereby we will show you how to do password-based and public key authentication with fabric, remote software installation with package managers, management of users and groups, management of file permissions, file uploads and downloads, configuration file manipulation with regular expressions (Python re module), serialization with pickle or JSON and manage communication between VMs. 

After this session you will know
* How to connect to OpenStack virtual machines via fabric API
* How to create private/public keypairs and authenticate to virtual machines
* How to combine fabric and cuisine to configure virtual machines
* How to use the Fabric API to employ package managers (like apt, yum, zypper, pacman) which install software packages on virtual machines
* How to add users and groups via Fabric to your virtual machines and set the right permissions to files and directories
* How to upload files to virtual machines or download files from virtual machines to your local computer
* How to use regular expressions and configuration file templates to create custom configuration files
* How to serialize objects with pickle or JSON and use serialization let VMs communicate to each other
