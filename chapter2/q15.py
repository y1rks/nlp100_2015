'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''
import sys

lineNum = int(sys.argv[1]) if len(sys.argv) == 2 else exit('Invalid args number')

with open('hightemp.txt') as f:
  text = f.readlines()
  length = len(text)
  for i in range(length):
    if length - i > lineNum:
      continue

    print(text[i], end='')
