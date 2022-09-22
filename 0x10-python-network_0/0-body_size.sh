#!/bin/bash
# sends a request to a give URL and displays size of body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
