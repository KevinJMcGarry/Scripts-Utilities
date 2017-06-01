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

git checkout master
git pull
# git merge origin/dev
git tag ${1}

git push origin master
git push origin tag ${1}
