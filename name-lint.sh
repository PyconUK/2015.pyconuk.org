#!/bin/bash

LINT[0]="$(egrep -R "Pycon UK" *.html *.rst)"
LINT[1]="$(egrep -R "pycon UK" *.html *.rst)"
LINT[2]="$(egrep -R "pyconUK" *.html *.rst)"

SUCCESS=0

for i in 0 1 2 ; do
    if [[ ${LINT[$i]} ]]; then
        echo "${LINT[$i]}"
        echo "Please spell the conference name PyCon UK."
        SUCCESS=1
    fi
done

exit $SUCCESS
