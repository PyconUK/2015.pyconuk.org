type: session
title: "Making code py2/3 compatible using python-future"
slug: "making-code-py23-compatible-using-python-future"
url: "talks/making-code-py23-compatible-using-python-future/index.html"
body_class_hack: talks
---

### Jørn Lomax

The talk will demonstrate how to port a Python2 project to python3. We will look at both making the code python3 exclusive, and making it cross compatible. This will be demonstrated using the python-future package, which is a camptibility library to aid with code porting. After this talk, you should be able to handle porting any python existing Py2 code to work with Py3.

This talk is based on work done during summer where the buildbot project was ported from Py2, to be cross compatible with Py3. It will demonstrate some of the challenges encountered and and some of the lessones learned during the process of porting both a small project (buildslave) and a large project (buildbot)
