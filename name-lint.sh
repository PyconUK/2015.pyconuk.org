#!/bin/bash

LINT="$(grep -e "Pycon UK" -e "pycon UK" -e "pyconUK" -e "PyConUK" \
        --line-number --recursive . \
        --include "*.html" --include "*.rst")"

SUCCESS=0

if [ ! -z $LINT ]; then
    echo "${LINT}"
    echo "Please spell the conference name PyCon UK."
    SUCCESS=1
fi

exit $SUCCESS
