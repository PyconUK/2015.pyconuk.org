type: session
title: "CPython memory internals"
slug: "cpython-memory-internals"
url: "talks/cpython-memory-internals/index.html"
body_class_hack: talks
---

### Francisco Fernández Castaño

Sometimes is interesting look under the hood and see how things work internally. 
We as python developers are lucky and we don't need to take care about handling
memory as a C/C++ developer must do. In this talk we'll explore how CPython handle
memory, how memory is allocated by the `Python memory manager`, the components that
are part of it, and how deals with various aspects, like sharing, segmentation, 
preallocation or caching. 