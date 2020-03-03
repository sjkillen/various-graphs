#/usr/env bash

cd "${0%/*}"

docker build --tag sjkillen/python3-graphviz .
docker push sjkillen/python3-graphviz
