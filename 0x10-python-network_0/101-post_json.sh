#!/bin/bash
# sends a JSON POST request, and displays the body of the response.
curl -s "$1" -X POST -d @"$2" -H "Content-Type: application/json"
