type: session
title: "Event-Sourced Domain Models in Python"
slug: "event-sourced-domain-models-in-python"
url: "workshops/event-sourced-domain-models-in-python/index.html"
body_class_hack: talks
---

### Robert Smallshire

#### Preparation

 * This is a *work*shop, not a lecture, so come with a laptop or pair-up with
 somebody who has one.

 * This workshop requires at least [Python 3.4](https://www.python.org/downloads/) so you should have a suitable interpreter installed.

 * Bring your favourite Python code editor.

 * Have the [workshop student materials](https://bitbucket.org/sixty-north/d5-workshop-exercises-student-material) installed from Bitbucket. Further instructions are to be found there.

 * You can also look at the [introductory slides](http://sixty-north.com/blog/event-sourced-domain-models-in-python-at-pycon-uk) which were used in the workshop.

#### Synopsis

In first part of this workshop we explore how to implement rich domain models using plain-old Python objects which are completely independent of any particular persistence technology such as an object-relational mapper.  Domain models often embody the core value of software systems, so implementing models independently of - often ephemeral - technology choices is an important strategy for long-lived, high-value systems.

In the second part of this workshop we implement an event-sourced architecture for persistence of our domain model, whereby all changes applied to the model are recorded as events in a simple, append-only event-store.  From this event store we can reconstitute the model state as it was at any historical time, something that is difficult – if not impossible – to do with most object-relational solutions.  Furthermore, we can project the event stream into other representations to support queries which are not conveniently supported by the entities in our model, or which roll-up historical data. Among many other benefits, such projected read-models gives very high scalability on the read-side.

This workshop is aimed at Python developers who want to step beyond the limits of canned framework-based solutions such as Django models, or toolkits such as SQLAlchemy, (which are ultimately about managing the horrors of shared-mutable state).  Event-sourced domain models facilitate allow us to combine the best aspects of object-oriented design with robust and simple persistence inspired by functional-programming practice.
