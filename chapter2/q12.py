'''
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
'''
import csv

fileName = 'hightemp.txt'
resultFile1 = 'col1.txt'
resultFile2 = 'col2.txt'

with open(fileName) as f:
  with open(resultFile1, mode='x') as rf1:
    with open(resultFile2, mode='x') as rf2:
      text = csv.reader(f, delimiter='\t')
      for row in text:
        rf1.write(row[0] + '\n')
        rf2.write(row[1] + '\n')
