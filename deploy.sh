#!/bin/bash

if [[ $TRAVIS = "true" ]]; then
	if [[ $TRAVIS_BRANCH = "master" && $TRAVIS_PULL_REQUEST = "false" ]]; then
		echo "Deploying!"
		# The output of this must be redirected to /dev/null to prevent leakage of $GH_TOKEN.
		git subtree push --prefix output https://PyConUK-user:$GH_TOKEN@github.com/PyconUK/pyconuk.org gh-pages >/dev/null
		if [[ $? -eq 0 ]]; then
			echo "Deployed successfully!"
		else
			echo "Deployment failed!"
		fi
	else
		echo "Not deploying!"
	fi
else
	git subtree push --prefix output origin gh-pages
fi
