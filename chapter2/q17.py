'''
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
'''
import csv

result = []

with open('hightemp.txt') as f:
  text = csv.reader(f, delimiter='\t')
  for row in text:
    if row[0] not in result:
      result.append(row[0])

for r in result:
  print(r)