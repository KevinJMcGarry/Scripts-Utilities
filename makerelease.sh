# Quick shell script for creating a Github release
# run the script passing in the tag as the first argument
# example makerelease.sh v1.10
# This process should be baked into the CI/CD pipeline but this script is good for quick release


#!/usr/bin/env bash

set -e

RED='\033[0;31m'
NC='\033[0m' # No Color
GREEN='\033[0;32m'

 echo -e "Be sure you are on the ${GREEN}master${NC} branch before running this script."

if [ -z "$1" ]
  then
    echo -e "${RED}No release specified${NC}"
fi

git checkout master  # switch to master branch
git pull origin master
git tag ${1}  # create new tag with argument given
git push origin tag ${1}  # push new tag to repo and create a release off of it
