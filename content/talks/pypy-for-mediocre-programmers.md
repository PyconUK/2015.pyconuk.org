type: session
title: "PyPy for mediocre programmers"
slug: "pypy-for-mediocre-programmers"
url: "talks/pypy-for-mediocre-programmers/index.html"
body_class_hack: talks
---

### Ronan Lamy

This is a talk for mediocre Python programmers by a mediocre programmer. PyPy is an alternative implementation of Python. It is notorious for being fast, but also for using clever algorithms pertaining to advanced concepts such as type inference, garbage collection, just-in-time compilation, etc. So, can we, mediocre programmers, realistically use PyPy?

Yes, absolutely. In fact, PyPy developers did all that hard work so that we wouldn't have to. As we'll see, it runs most Python code exactly like CPython does, save that it magically makes it faster.

Porting existing applications is always more involved than running a simple script, so we'll also examine likely difficulties such as code relying on CPython implementation details, and dependencies on C extensions, and explore simple principles to let PyPy run your code even faster.

Finally, we'll have a glimpse of the future by looking at what's brewing in the PyPy lair, such as software transactional memory, new speed optimisations, better support for Python 3 and NumPy, ...