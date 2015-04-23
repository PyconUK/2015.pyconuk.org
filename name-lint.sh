#!/bin/bash

LINT0="$(egrep "Pycon UK" *.html *.rst -R)"
LINT1="$(egrep "pycon UK" *.html *.rst -R)"
LINT2="$(egrep "pyconUK" *.html *.rst -R)"

SUCCESS=0

if [[ $LINT0 ]]; then
    echo $LINT0
    echo "Please spell the conference name PyCon UK."
    SUCCESS=1
fi
if [[ $LINT1 ]]; then
    echo $LINT1
    echo "Please spell the conference name PyCon UK."
    SUCCESS=1
fi
if [[ $LINT2 ]]; then
    echo $LINT2
    echo "Please spell the conference name PyCon UK."
    SUCCESS=1
fi

exit $SUCCESS
