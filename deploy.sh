#!/bin/bash

if [[ $TRAVIS = "true" ]]; then
	if [[ $TRAVIS_BRANCH = "master" && $TRAVIS_PULL_REQUEST = "false" ]]; then
		echo "Deploying!"
		git subtree push --prefix output https://PyConUK-user:$GH_TOKEN@github.com/PyconUK/pyconuk.org gh-pages
	else
		echo "Not deploying!"
	fi
else
	git subtree push --prefix output origin gh-pages
fi
