type: session
title: "Extending Python"
slug: "extending-python"
url: "talks/extending-python/index.html"
body_class_hack: talks
---

### Francisco Fernández Castaño

Python is a great language, but there are occasions where we need access to low
level operations or connect with some database driver written in C or we need to
overcome to some speed boottleneck in Python due to some limitation in the
language, like NumPy or Scikit-learn do, using extensions.

With the FFI(Foreign function interface) we can connect Python with other
languages like C, C++ and even Rust or Fortran.
There are some alternatives to achieve this goal, Native Extensions, Ctypes and CFFI.
We'll compare this three ways of extending Python and we'll study pros and cons
of each approach.
