PyconUK website
===============

.. image:: https://travis-ci.org/PyconUK/pyconuk.github.io.svg?branch=master
       :target: https://travis-ci.org/PyconUK/pyconuk.github.io

This is the website for PyconUK. It is hosted via GitHub Pages and available via http://pyconuk.org/.

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

Usage
-----

Installation
~~~~~~~~~~~~
This site uses Jekyll_ and we've wrapped the development environment in Docker.

0. (OS X only) Install boot2docker_ (you can also homebrew it)
1. Install docker_
2. Build the docker image (this may take some time): ``docker build -t pyconukorg .``
3. Run the docker image: ``docker run -p 80:4000 -ti pyconukorg``
4. Get your docker ip: ``docker ip`` (or ``boot2docker ip`` if you're using that)
5. Open your web browser of choice and go to the IP from step 4


Development
~~~~~~~~~~~
Pages are essentially `Liquid templates`_. Essentially stick some YAML front-matter at the start containing page metadata (like `layout` and `title`) at the top of a Markdown / HTML file of content.

Travis will test branches, and branches won't get merged without review and passing tests, so dive right in!

.. _Jekyll: http://jekyllrb.com/
.. _boot2docker: http://docs.docker.com/installation/mac/
.. _docker: https://docs.docker.com/installation/#installation
.. _rvm: https://rvm.io/
.. _rbenv: http://rbenv.org/
.. _bundler: http://bundler.io/
.. _Liquid templates: http://jekyllrb.com/docs/templates/
