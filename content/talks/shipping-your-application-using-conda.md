type: session
title: "Shipping your application using Conda"
slug: "shipping-your-application-using-conda"
url: "talks/shipping-your-application-using-conda/index.html"
body_class_hack: talks
---

### Floris Bruynooghe

Shipping your Python application to customers has always been an
interesting challenge.  Many Operating Systems ship with a Python
version, but they only ship that to support their applications and it
will probably miss dependencies you need or be the wrong version.  So
you need to build and ship your own Python environment, but one which
can work on all these different platforms.  This is never easy.

Recently Continiuum Analytics have released their Conda package
manager as open source, which is very well suited to address this
problem.  It has support for building and distributing binary packages
and is capable of creating a stand-alone environment for your
application with no or minimal dependencies on the host OS.  But even
starting from a good tool there are still a lot of tricks to building
a good Python distribution.  This talk will concentrate on UNIX
platforms and dive into the details of what needs to be done to create
a portable distribution.  It will then discuss how to fully bootstrap
such a distribution using Conda.