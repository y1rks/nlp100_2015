#!/bin/bash

# この処理方法だと分割結果が異なる。例えば7の時ファイルが8分割される。(正確なN分割は、splitを使っては実現できない気がする)

lineNum=`wc -l hightemp.txt | awk '{print $1}'`
splitLineNum=`expr $lineNum / $1`

split -l $splitLineNum hightemp.txt