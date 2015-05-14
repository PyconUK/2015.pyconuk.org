PyCon UK website
================

.. image:: https://travis-ci.org/PyconUK/pyconuk.github.io.svg?branch=master
       :target: https://travis-ci.org/PyconUK/pyconuk.github.io

This is the website for PyCon UK. It is hosted via GitHub Pages and available via http://pyconuk.org/.

We welcome pull requests for improvements! (Please see CONTRIBUTING.rst for details.)

Use the following process to submit changes:

* Fork the repository.
* Create a descriptive branch name for the change you are proposing.
* Push your changes in your local branch back to your remote GitHub repository.
* In GitHub, create a pull request from your branch against our upstream repository.
* Someone (not you) will check the change and either merge it (thus automatically updating the website) or add comments for further changes or a reason for rejection.

If you're not a coder please feel free to create issues here: https://github.com/PyconUK/pyconuk.github.io/issues

That's it!

:-)


Development
~~~~~~~~~~~
This site uses wok_.  To install wok and other dendencies, run ``pip install -r requirements.txt``.

wok builds the site by assembling several components:

* Pages are found in ``content/``.  Pages may be HTML, Markdown_ or reStructuredText_, and contain some YAML metadata.
* Static files are found in ``media/``.
* A jinja2_ template for all the pages is found in ``templates/default.html``

To build the site, run ``make build``.  This will pull together all the componenents into a set of HTML files in ``output/``.

Alternatively, if you run ``make serve``, wok will build the site, serve the built site on port 8000, and watch for changes.

It is the ``output/`` directory that gets served by GitHub pages, so please make sure this is included when you submit your pull request.

Travis will test branches, and branches won't get merged without review and passing tests, so dive right in!

.. _wok: http://wok.mythmon.com/
.. _Markdown: https://pythonhosted.org/Markdown/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _jinja2: http://jinja.pocoo.org/
