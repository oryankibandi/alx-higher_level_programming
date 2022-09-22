#!/usr/bin/env bash
# displays the body of a response only with 200 response
curl -s "$1" -X GET -L
