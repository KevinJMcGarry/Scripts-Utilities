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
git push origin tag ${1}
