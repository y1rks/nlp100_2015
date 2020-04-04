#!/bin/bash

cut -f 1 hightemp.txt | sort | uniq -c | sort -rk 1