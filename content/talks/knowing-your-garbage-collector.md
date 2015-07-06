type: session
title: "Knowing your Garbage collector"
slug: "knowing-your-garbage-collector"
url: "talks/knowing-your-garbage-collector/index.html"
body_class_hack: talks
---

### Francisco Fernández Castaño

As Python programmers we're used to program without taking care about allocating
memory for our objects and later on freeing them, Python garbage collector
takes care of this task automatically for us.

Garbage collection is one of the most challenging topics in computer science,
there are a lot of research around the topic and different ways to tackle
the problem.

Knowing how our language does this process give us a better understanding
of underlying interpreter and allow us to know why problems like cycles
can happen in CPython interpreters.

So, this talk aims to be and introduction to the topic and a walkaround
through different approaches followed in CPython and PyPy:

* Generational Reference counting with cycles detector on CPython.
* Incremental version of the MiniMark GC on PyPy.
