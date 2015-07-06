type: session
title: "You Don’t Care About Efficiency: Synchronous Code Is Dying"
slug: "you-dont-care-about-efficiency-synchronous-code-is-dying"
url: "talks/you-dont-care-about-efficiency-synchronous-code-is-dying/index.html"
body_class_hack: talks
---

### Cory Benfield

If you write blocking code, you don’t care about efficiency.

There, I said it.

It’s 2015, and still the vast majority of Python programmers write essentially synchronous code that blocks on network I/O. This approach, while simple to reason about, struggles mightily with scaling up and out into software that does a lot of network I/O. Worse, it makes it difficult to write code that reacts rapidly to changing conditions.

The writing is on the wall for this kind of software, as the community shifts towards writing software that embraces asynchronicity. In this talk we’ll discuss why synchronous software is a problem, what your options are to move away from it, and what challenges are being faced by the Python ecosystem as we try to move towards a brave new asynchronous world.