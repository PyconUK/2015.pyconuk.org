#!/bin/bash

if [[ $TRAVIS = "true" ]]; then
	if [[ $TRAVIS_BRANCH = "master" && $TRAVIS_PULL_REQUEST = "false" ]]; then
		echo "Deploying!"

		# Set up credentials for pushing to GitHub.  $GH_TOKEN is
		# configured via Travis web UI.
		git config credential.helper "store --file=.git/credentials"
		echo "https://PyConUK-user:$GH_TOKEN@github.com" > .git/credentials

		# Set up config for committing.
		git config user.name "Travis"
		git config user.email "no-reply@pyconuk.org"

		# Check out master (because currently HEAD is detached, level
		# with master), then add, commit, and push any changes to the
		# output directory introduced by this change.  The output
		# directory will have been updated (if required) when
		# pre-flight-checks.sh ran.  If the output directory is already
		# up to date then no new commit will be made.
		git checkout master
		git commit -a -m "[skip ci] Travis auto-commit.  Built latest changes."
		git push https://PyConUK-user@github.com/PyconUK/pyconuk.org master

		# Push output directory to gh-pages branch on GitHub.
		git subtree push --prefix output https://PyConUK-user@github.com/PyconUK/pyconuk.org gh-pages

		# Clean up.
		rm .git/credentials
	else
		echo "Not deploying!"
	fi
else
	git subtree push --prefix output origin gh-pages
fi
