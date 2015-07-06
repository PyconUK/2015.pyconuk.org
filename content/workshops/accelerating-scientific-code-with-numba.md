type: session
title: "Accelerating Scientific Code with Numba"
slug: "accelerating-scientific-code-with-numba"
url: "workshops/accelerating-scientific-code-with-numba/index.html"
body_class_hack: talks
---

### Graham Markall

This tutorial will provide an overview of Numba, a just-in-time Python compiler focused on numerical computing. Originally aimed at computations using Numpy arrays, it has been expanded to work with other Python types and can speed up computations that require more than just fast linear algebra operations. Numba targets both CPUs and CUDA GPUs by generating native code using the LLVM compiler infrastructure.

This introduction aims to span the breadth of use cases rather than focusing on a single area in depth. This is in order to enable the selection of appropriate portions of code to use with Numba, and the correct selection of Numba's facilities in each case.

Areas that will be covered include:

* An overview of the type system, with a view to understanding and overcoming typing issues,
* Compilation of Python functions using the @jit decorator,
* Creation of Numpy ufuncs in Python using the @vectorize decorator,
* Understanding the performance of compiled code, and performance optimisation tips,
* Debugging facilities in Numba.

This tutorial is intended for an audience of programmers and data scientists who have an interest in speeding up numerical routines, and people with a general interest in high-performance Python. In order to get started quickly, it is recommended that attendees install the Anaconda Python distribution or Miniconda, as this provides a robust mechanism for installing Numba on Linux, Mac OS X and Windows.
