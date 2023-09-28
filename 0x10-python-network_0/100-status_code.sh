#!/bin/bash
#sends GET request to a given URLL and display the response status
curl -s -o /dev/null -w "%{http_code}" "$1"
