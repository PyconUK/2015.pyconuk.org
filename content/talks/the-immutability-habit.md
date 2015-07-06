type: session
title: "The Immutability Habit"
slug: "the-immutability-habit"
url: "talks/the-immutability-habit/index.html"
body_class_hack: talks
---

### Dan Clark

When did you last build a system which stores every version of each change indefinitely and can present a view of the data at any point in time?

Relatively few apps are built with "append only" data structures yet it's something that has become easier with modern technology and can bring enormous benefit. This talk will cover the rationale for doing so, plus a concrete example of how to do this using a document database, MongoDB.

We'll look at transactional and concurrency concerns and also extend the example to publishing real-time updates (using redis and WebSockets) to keep users in sync.