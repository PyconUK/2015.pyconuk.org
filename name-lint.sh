#!/bin/bash

LINT[0]="$(egrep "Pycon UK" -r *.html *.rst)"
LINT[1]="$(egrep "pycon UK" -r *.html *.rst)"
LINT[2]="$(egrep "pyconUK" -r *.html *.rst)"
LINT[3]="$(egrep "PyConUK" -r *.html *.rst)"

SUCCESS=0

for i in 0 1 2 3 ; do
    if [[ ${LINT[$i]} ]]; then
        echo "${LINT[$i]}"
        echo "Please spell the conference name PyCon UK."
        SUCCESS=1
    fi
done

exit $SUCCESS
