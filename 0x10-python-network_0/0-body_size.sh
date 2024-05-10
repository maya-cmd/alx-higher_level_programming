#!/bin/bash
# URL, sends a request to that URL, and
# It also,displays the size of the body of the response
curl -sI "$1" | awk '/Content-Length/{print $2}'
