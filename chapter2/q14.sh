#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Invalid args number" 1>&2
  exit 1
fi

head -n $1 hightemp.txt