#!/bin/bash

lineNum=`wc -l hightemp.txt | awk '{print $1}'`
splitLineNum=`expr $lineNum / $1`

split -l $splitLineNum hightemp.txt