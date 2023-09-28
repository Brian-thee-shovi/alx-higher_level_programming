#!/bin/bash
# It takes URL, SENDS REQUEST TO THE URL and displays content lenght
curl - sI "$1" | grep 'Content-Length:' | cut - c 17-
