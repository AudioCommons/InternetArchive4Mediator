#! /bin/bash

# output redirection with '> out.txt'
curl -v -H POST "http://localhost:8331/transform" --data-urlencode query@$1
