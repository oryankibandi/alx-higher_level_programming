#!/bin/bash
# sends a GET request with header X-School-User-Id:98
curl -sH "X-School-User-Id: 98" -X GET "$1"
