type: session
title: "Unit test documentation improvements"
slug: "unit-test-documentation-improvements"
url: "sprints/unit-test-documentation-improvements/index.html"
body_class_hack: talks
---

### Tibs

I use the standard library Python unittest package. Various assertXXX methods take two arguments, one "expected" and one "actual". The documentation doesn't give any indication which is which, but the output produced assumes you knew.
The sprint would be to work out the necessary changes to the documentation, determine if the module docstrings also needed changing, and perhaps whether the method arguments should/could be renamed, finishing with putting together a patch submission (or whatever the appropriate mechanism is). It could be a one person task, but would work better with two, to make sure the results make sense.