type: session
title: "Testing with two failure seeking missiles: fuzzing and property based testing"
slug: "testing-with-two-failure-seeking-missiles-fuzzing-and-property-based-testing"
url: "talks/testing-with-two-failure-seeking-missiles-fuzzing-and-property-based-testing/index.html"
body_class_hack: talks
---

### Tom Viner

Testing with purely random data on it's own doesn't get you very far. But
two approaches that have been around for a while have new libraries that
help you generate random input, that homes in on failing testcases.

First **[Hypothesis](https://hypothesis.readthedocs.org/en/latest/)**, a Python implementation and update of the Haskell library QuickCheck. Known as property based testing, you specify a property of your
code that must hold, and Hypothesis does its best to find a counterexample.
It then shrinks this to find the minimal input that contradicts your property.

Second, **[American fuzzy lop](http://lcamtuf.coredump.cx/afl/)** (AFL), is a young fuzzing library that's already
achieved an impressive trophy case of bug discoveries. Using
instrumentation and genetic algorithms, it generates test input that
carefully searches out as many code paths as it can find, seeking greater
functional coverage and ultimately locating crashes and hangs that no other
method has found. I'll be showing how with **[Python-AFL](http://jwilk.net/software/python-afl)** we can apply this
tool to our Python code.
