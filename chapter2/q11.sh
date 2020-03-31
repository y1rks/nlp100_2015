#!/bin/bash

cat hightemp.txt | sed s/$'\t'/$' '/g