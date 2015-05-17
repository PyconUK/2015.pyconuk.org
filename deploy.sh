#!/bin/bash

if [[ $TRAVIS = "true" ]]; then
	if [[ $TRAVIS_BRANCH = "master" && $TRAVIS_PULL_REQUEST = "false" ]]; then
		echo "Deploying!"
		git config credential.helper "store --file=.git/credentials"
		echo "https://$GH_TOKEN:@github.com" > .git/credentials
		git subtree push --prefix output https://PyConUK-user@github.com/PyconUK/pyconuk.org gh-pages
		rm .git/credentials
	else
		echo "Not deploying!"
	fi
else
	git subtree push --prefix output origin gh-pages
fi
