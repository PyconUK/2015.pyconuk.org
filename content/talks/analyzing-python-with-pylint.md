type: session
title: "Analyzing Python with Pylint"
slug: "analyzing-python-with-pylint"
url: "talks/analyzing-python-with-pylint/index.html"
body_class_hack: talks
---

### Claudiu Popa

Given the dynamic nature of Python, some bugs tend to creep in our codebases. Innocents NameErrors or hard-to-find bugs with variables used in a closure, but defined in a loop, they all stand no chance in front of Pylint (http://pylint.org/).

In this talk, I’ll present one of the oldest static analysis tools for Python, with emphasis on what it can do to understand your Python code. Pylint is both a style checker, enforcing PEP 8 rules, as well as a code checker in the vein of pyflakes and pychecker, but its true power isn’t always obvious in the eye of beholder, especially when it's hidden through its verbosity. Interpreting its results can be a daunting task, but there are tricks which can be used to improve its user experience, such as enabling only structural checking with the -E flag or disabling unwanted category checks.

Pylint can detect simple bugs such as unused variables and imports, but it can also detect more complicated cases such as invalid arguments passed to functions, it understands the method resolution order of your classes, generators, contexts managers and what special methods aren’t implemented correctly.

Starting from abstract syntax trees, we’ll go through its inference engine and we’ll see how Pylint understands the logical flow of your program and what sort of type hinting techniques are used to improve its inference, including PEP 484 type hints. Pylint's roadmap includes better understanding of Python code, by improving its flow control analysis, escape analysis, understanding metaclasses and descriptors and having a better type checker, as well as improving the user experience, by reducing the number of false positives it currently has. As a bonus, I’ll show how it can be used to help you port your long-forgotten library to Python 3, using its new –py3k mode, which emits warnings regarding Python 3 compatibility.

The participants should have a basic understanding of Python. No other prerequisite is necessary, since the other concepts will be explained during the talk.

The following concepts will be explained during this talk:

  -   abstract syntax trees
   -  static analysis and why using static analysis for your code
   -  what is inference and what forms an inference engine
