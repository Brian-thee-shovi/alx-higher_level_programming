#!/bin/bash
# displlays all HTTP methods the server of given URL would accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
