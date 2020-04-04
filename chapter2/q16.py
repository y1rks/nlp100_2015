'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
'''

import sys
import numpy as np

splitNum = int(sys.argv[1]) if len(sys.argv) == 2 else exit('Invalid args number')

with open('hightemp.txt') as f:
  text = f.readlines()
  lineNum = len(text)
  count = 0
  for splitedFile in np.array_split(text, splitNum):
    with open('q16_result_{num}'.format(num=count), mode='x') as r:
      for line in splitedFile:
        r.write(line)
      count += 1
