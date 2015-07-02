title: Abstracts
slug: abstracts
body_class_hack: talks
---

Abstracts
=========

Brief outlines of each event will follow, especially check
back in the weeks before the conference to see what has been
added.

PyCon UK is an informal yet exciting mix of talks, tutorials,
workshops, keynotes, socials, plenary hi-jinks, five minute 'lightning
talks' and more.

Please see our `YouTube channel`_ to see a few of the things we got up
to last year.

Friday has talks and workshops from Python experts from the UK and
further afield as well as a special `Python in Education`_
track. The day will be rounded off with a bring-your-own buffet charity
event in memory of John Pinner (all proceeds to be donated to Cancer
Research UK).

Saturday contains more talks, workshops and networking but also the
Lightning Talk Man takes flight and the kids outsmart us all in the
special Children's Track, the science track begins and all this is
followed by the PyCon UK Conference Dinner.

Sunday contains the PyCon UK Panel, a 'Question Time' style event
where you can ask leading Python developers questions on Python,
developing and the meaning of life. Lightning Talk Man continues to
inspire and entertain and we hold the all-important PyCon UK jobs fair
where you can recruit or be recruited from a pool of the highest
quality UK developers.

Monday is the Sprint day, we split into small groups and in each group
a member of an Open Source Python project guides a small group in how
to hack on the project. Improve your Python skills in a fun, practical
and effective way.

Keynotes
~~~~~~~~

To be announced.

Socials
~~~~~~~

.. _dinner:

The PyCon UK Dinner
-------------------

Details of the dinner will be published here.

.. _social:

The Friday Night Social
-----------------------

.. _mellow:

The Mellow Night
------------------

Details of where to collapse in a heap of tired out
developers will be published here.

Plenary Sessions
~~~~~~~~~~~~~~~~

.. image:: http://www.lightningtalkman.com/harald1.png
    :align: right
    :alt: Image of Lightning Talk Man
    :width: 315
    :height: 400

.. _lightningtalks:

The Lightning Talk Show
-----------------------

Lightning Talks are speeches limited to 5 minutes, covering any topic.

The Lightning Talk Man orchestrates the proceedings. He ensures that
timing is kept and links the talks with his own stories. That way he
keeps the audience attentive, forms the aesthetics and promotes the
speakers.

From Stuttgart, Germany, Harald Armin Massa has been the MC of the
PyCon UK lightning talks since PyCon UK hosted Europython in 2009 and
2010 and we decided we like him so much that we had to keep him.

.. _panel:

The PyCon UK Panel
~~~~~~~~~~~~~~~~~~

In the style of Question Time (or Gardeners' Question Time, but
without the plants), PyCon UK's acting Chair Zeth chairs a panel of
five Python experts who each give an short overview of how they found
the conference and then try to answer your questions about the future
of Python, Software development and the meaning of life, the universe
and everything.

The PyCon UK panel will probably include:

 * Michael Foord: Python core developer and Go programmer. Works for
   Canonical, knows more than is healthy about Python testing and Cloud
   computing.

 * Sarah Mount: Senior Lecturer in Computer Science at the University
   of Wolverhampton. Loves to talk about distributed Python and
   concurrency. Is Chair of the science track at PyCon UK.

 * Van Lindberg is a smiley chap and Vice President of Intellectual
   Property at Rackspace and chairman of the PSF.

 * Larry Hastings is one of the main CPython core contributors and the
   Release Manager for Python releases.

 * A currently unselected Djangogirls organiser

Python for Science
~~~~~~~~~~~~~~~~~~

Python for science is open to all delegates but particularly aimed at
scientists of all kinds, data scientists, researchers and professional
software engineers on Python in the science field.

.. _form:

Forming a PyCon UK research community
-------------------------------------

*Dr Sarah Mount, Wolverhampton University*

Sarah opens the Science Track by introducing the workshops, talks and
sprint and discusses the formation of a research community.

.. _numba:

Accelerating Scientific Code with Numba
---------------------------------------

*Graham Markall*

This tutorial will provide an overview of Numba, a just-in-time Python
compiler focused on numerical computing. Originally aimed at
computations using Numpy arrays, it has been expanded to work with
other Python types and can speed up computations that require more
than just fast linear algebra operations. Numba targets both CPUs and
CUDA GPUs by generating native code using the LLVM compiler
infrastructure.

This introduction aims to span the breadth of use cases rather than
focusing on a single area in depth. This is in order to enable the
selection of appropriate portions of code to use with Numba, and the
correct selection of Numba's facilities in each case.

Areas that will be covered include:

 * An overview of the type system, with a view to understanding and overcoming typing issues,
 * Compilation of Python functions using the @jit decorator,
 * Creation of Numpy ufuncs in Python using the @vectorize decorator,
 * Understanding the performance of compiled code, and performance optimisation tips,
 * Debugging facilities in Numba.

This tutorial is intended for an audience of programmers and data
scientists who have an interest in speeding up numerical routines, and
people with a general interest in high-performance Python. In order to
get started quickly, it is recommended that attendees install the
Anaconda Python distribution or Miniconda, as this provides a robust
mechanism for installing Numba on Linux, Mac OS X and Windows.

.. _testing:

Getting started with testing scientific programs
------------------------------------------------

*Martin Jones*

When writing programs for scientific research, we tend to be focussed
on getting results, so testing is generally not a priority. Often,
this means that our data-processing pipelines end up incorporating
programs that don't have test suites. Examples of high-profile
retractions due to software errors
(e.g. http://www.sciencemag.org/content/314/5807/1856.full) illustrate
the dangers of this approach.

This session will be a gentle introduction to testing, aimed at people
writing scientific software who would like to start taking advantage
of automated testing. We'll start with Python’s built-in tools and
moving on to using the Nose testing framework. We’ll look at the
problems that testing can solve, and see some best-practises for
writing tests.

The goal of this training session is for attendees to come away
with (1) an understanding of some basic testing concepts, (2) some
hands-on experience of running tests and interpreting the output,
and (3) an idea of how to start applying these tools to their own
projects.

Attendees should have a basic knowledge of Python and should be
familiar with the idea of functions, conditions and exceptions. They
should also have the Nose package installed (pip install nose should
work in most cases).

.. _titfortat:

Tit for Tat, Evolution, Game Theory and the Python Axelrod Library
------------------------------------------------------------------

*Vince Knight*

This talk will begin with the origin of species. More precisely with a
discussion of Darwin's theory of evolution and how Game Theory has
been used to explain/illustrate aspects of cooperation in complex
dynamics.

In 1980, professor Robert Axelrod created a computer tournament
inviting submissions of code snippets that would compete against each
other. A large amount of academic study has concentrated on the
outcomes of this experiment. The particularity of the outcome, was
that even when the tournament was repeated with a much larger number
of strategies, a very simple strategy was victorious: Tit for
Tat. This strategy tries it's best to cooperate with other strategies!

The talk will briefly discuss all of this but will concentrate on a
new Python library (pip install axelrod). This project, hosted on
github allows anyone to recreate the tournament but also (and arguably
more importantly) submit strategies via pull request!

It is anticipated that this talk would be appreciated by coders of all
levels as it gives a very low entry level for a contribution to an
open source project. It should also be of interest to the more
experienced coders as it is hoped that novel strategies will be
devised and submitted. Indeed, historically strategies have been
mainly devised by mathematicians and economists, surely the pyconuk
attendees will bring something new to the repository?

Finally, for those who are perhaps not interested in 'playing along'
the talk will also describe the newest addition to the project which
is a Django project aiming to bring this study of evolution to a
popular audience.

.. _ship:

Ship Data Science Products!
---------------------------

*Ian Ozsvald*

Building and shipping working Data Science and scientific products is
hard - learn from 10 years of Ian's experience at ModelInsight.io to
find efficient ways through the mess of bad data, complicated data
workflows and weakly designed code through to successfully deployed
projects.

This talk will include ways of getting data, cleaning and debugging
it, approaches to deployment and various tips I've picked up along the
way that'll save you lots of time.

If you're fresh out of academia and want to do science then this will
open your eyes to how 'stuff works in industry'. If you're in a
growing data science team and you want to do more science and spend
less time fighting fires - this talk is definitely for you. Be more
effective, stop fighting fires and burning time.

Ian Ozsvald is co-founder of the 1,500+ member PyDataLondon meetup and
conference series, a published O'Reilly author, international speaker
and teacher and he runs a 10 year old Data Science consulting group in
London (ModelInsight.io).

.. _ice:

iCE: Interactive cloud experimentation
--------------------------------------

*George Lestaris*

In the cloud-computing era, many technologies like Puppet, chef,
ansible, etc arose to take care of setting up, maintaining and
provisioning virtual machine clusters. However these tools do not
prove to be practical for cases where the user wants to test a
deployment or try a small experiment involving many VMs in the
cloud. Additionally they lack interactiveness and the user is unable
to hijack or influence the deployment process during runtime.

Python iCE is a tool that aims to enable interactive cloud
experimentation. It can deploy VM clusters in EC2-compatible public
clouds and allow the user to manage them through SSH. It formalises an
experiment as a Python script with fabric tasks which can run on every
or selected VMs in a cluster.

It also integrates with IPython and it has its own shell that allows
for interactive handling of the VMs. iCE is built with
well-established Python libraries like IPython, boto and fabric.

iCE comes with a lightweight agent that registers a VM to an
experiment’s pool. This agent will run automatically for VMs deployed
with iCE but users can manually run it on already running VMs to
utilise them through iCE.

It's IPython shell facilitates the development and execution of
experiments. Its main goal is to bring the ease of use and
interactiveness of single-machine SSH sessions to virtual clusters.

.. _power:

Power: Python in Astronomy
--------------------------

*Tomas James*

The universe is a wild and wonderful place. From the quantum
mechanical effects that power the Sun, to the gravitational effects
that suck everything in to a black hole, one thing links them all:
they can all be analysed using Python.

Python’s clear syntax and extensibility makes it an incredibly usable
and streamlined language for scientists. We’ll cover off exactly how
scientists use Python, what Python can do that other languages can’t,
and just how you can use a simple Python script to generate beautiful
astronomical images from the comfort of your favourite armchair.

.. _earthquakes:

Pythons and Earthquakes
-----------------------

*Girish Kumar*

In this session, we will cover how Python is used in providing
near-real-time maps of landslide hazard following large
earthquakes. Our tool is called 'shakeslide' for post-disaster
response, analysis and research and I will discuss the process of how
a research paper was converted into a functional web application

.. _meaning:

Getting meaning from scientific articles
----------------------------------------

*Eleonore Mayola*

The bibliography process means every scientist regularly has to go
through a lot of published articles in parallel to her/his
research. The aim is 1) to know what other researchers are doing: they
might be ahead of you, they might have proven your project is a dead
end, 2) get some context to interpret your research results. Using
specialised search engines can be inefficient if you don't use the
"right" keywords. Researcher also tend to find bibliography boring so
it would be interesting to automate part of the process!

In my talk I'll answer the following question: can Python machine
learning libraries (nltk, scikit-learn) be used to determine whether a
research article is worth reading? I'll use the Natural Language
Processing to identify articles topics and train a classifier to
distinguish between relevant and non-relevant articles depending and
someone's area of research.


Lunchtime events
~~~~~~~~~~~~~~~~

.. _poster:

The PyCon UK Poster Session
---------------------------

.. _jobfair:

The PyCon UK Job Fair
---------------------

Get recruited by one of our sponsors! Dozens of people have gotten
jobs because of connections made at PyCon UK, although sometimes in
the corridor or socials! Come and meet our sponsor companies and also
meet with fellow Python developers for tips on the all important
Python Job Market.

.. _singleboard:

Single Board Computer Hackspace
-------------------------------

Time to get tangible and share what you have made with your
Raspberry Pi, Arduino, Beagle Board, re-engineered phone or
other embedded or otherwise interesting hardware project.

.. _codeclinic:

Code Clinic
-----------

.. _dojo:

Python Dojo
-----------
