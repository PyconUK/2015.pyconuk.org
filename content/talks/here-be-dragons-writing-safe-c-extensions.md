type: session
title: "Here be Dragons - Writing Safe C Extensions"
slug: "here-be-dragons-writing-safe-c-extensions"
url: "talks/here-be-dragons-writing-safe-c-extensions/index.html"
body_class_hack: talks
---

### Paul Ross

Writing Python C Extensions can be daunting; you have to embrace not just C but Python's C API, which is huge. Not only do you have to worry about just your standard malloc() and free() but now you also have to contend with how CPython manages its memory.

This talk describes what you need to know to write fast ,reliable Python extensions in 'C'. It demonstrates some of the pitfalls you can encounter and some simple and robust coding patterns that you can use to avoid them. After this talk you will be able to write Python extensions with confidence.

This talk is largely based on [this material][1] and some hard won industrial experience.

  [1]: https://github.com/paulross/PythonExtensionPatterns