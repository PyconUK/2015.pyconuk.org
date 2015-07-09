type: session
title: "iCE: Interactive cloud experimentation"
slug: "ice-interactive-cloud-experimentation"
url: "talks/ice-interactive-cloud-experimentation/index.html"
body_class_hack: talks
---

### George Lestaris

In the cloud-computing era, many technologies like Puppet, chef, ansible, etc arose to take care of setting up, maintaining and provisioning virtual machine clusters. However these tools do not prove to be practical for cases where the user wants to test a deployment or try a small experiment involving many VMs in the cloud. Additionally they lack interactiveness and the user is unable to hijack or influence the deployment process during runtime. Python iCE is a tool that aims to enable interactive cloud experimentation. It can deploy VM clusters in EC2-compatible public clouds and allow the user to manage them through SSH. It formalises an experiment as a Python script with fabric tasks which can run on every or selected VMs in a cluster. It also integrates with IPython and it has its own shell that allows for interactive handling of the VMs. iCE is built with well-established Python libraries like IPython, boto and fabric.

iCE comes with a lightweight agent that registers a VM to an experiment’s pool. This agent will run automatically for VMs deployed with iCE but users can manually run it on already running VMs to utilise them through iCE. Its IPython shell facilitates the development and execution of experiments. Its main goal is to bring the ease of use and interactiveness of single-machine SSH sessions to virtual clusters.