'''
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
'''
import csv, operator

result = {}

with open('hightemp.txt') as f:
  tsvFile = csv.reader(f, delimiter='\t')
  for row in tsvFile:
    if row[0] in result.keys():
      result[row[0]] += 1
    else:
      result[row[0]] = 1

for ele in sorted(result.items(), key=operator.itemgetter(1), reverse=True):
  print(str(ele[1]) + '\t', end='')
  print(ele[0])
