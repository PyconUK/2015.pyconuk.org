type: session
title: "Dispelling py.test magic"
slug: "dispelling-pytest-magic"
url: "talks/dispelling-pytest-magic/index.html"
body_class_hack: talks
---

### Tomek Paczkowski

This short talk will look under the hood of how py.test uses assertion
statement rewriting to give users a better, more pythonic testing experience. 

Usually in Python, assertion statements are quite simple and tedious to work
with, where a simple snippet of code like this:

    def double(x):
        return x * 2
    expected = 5
    assert double(2) == expected

finishes with message that does not include any context:

    Traceback (most recent call last):
      File "t.py", line 5, in <module>
        assert double(2) == expected
    AssertionError

With py.test, we get a lot more information with all intermittent values nicely
described:

    t.py:5: in <module>
        assert double(2) == expected
    E   assert 4 == 5
    E    +  where 4 = <function double at 0x1033add08>(2)

During this talk you will learn about all the ingredients needed to
reverse-engineer py.test behaviour, using import hooks described in PEP 302,
and the ast module from standard library. We will try to use these hidden gems
in a broader context, outside of testing.
