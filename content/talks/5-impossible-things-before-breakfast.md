type: session
title: "5 impossible things before breakfast"
slug: "5-impossible-things-before-breakfast"
url: "talks/5-impossible-things-before-breakfast/index.html"
body_class_hack: talks
---

### Michael Sparks

Sometimes you're asked to deliver something that seems impossible, but
necessary in a given timeframe.  Sometimes it's several seemingly impossible
things.

Developing the prototype for the BBC Micro:bit - a pocket sized, child
programmable computer - was very much like this.  It had 3 months to be
delivered in a form sufficiently robust and usable to be used by children in
schools across the country; to be sufficiently documented to be completely
understood from scratch by others; and to be a sufficiently open and
flexible design to allow any and all parts of the system to change, while
retaining its core principles.

There was about 3 months to develop the entire stack from scratch. This
included a microcontroller based hardware stack, through firmware, a python
to C++ compiler (3-4 weeks), through django website, through to a QT
(PySide) client side application, through to publication of the device as a
network connected and controllable device via REST.  Python was involved in
all layers - including at microcontroller level on a device too small to run
any python interpreter.

The bulk of the development period had just one developer for hardware
and software.  For just 1 month there were 2 extra developers brought on
board, part time to assist.

This talk will be a detailed overview of the various subsystems, and the
strategies taken to deliver a complete, mass produce-able, and sufficiently
scalable product such an aggressive timescale.  The talk title is a nod to
the idea that while each of the various layers is doable alone in 3 months,
doing all the layers simultaneously using one developer is ... challenging.

It should be of interest to those interested in developing hardware and
software products, and especially those developing products that have both a
hardware and software element.
