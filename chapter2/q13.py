'''
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
'''

col1 = open('col1.txt').readlines()
col2 = open('col2.txt').readlines()
result = open('q13_result.txt', mode='x')

for i in range(len(col1)):
  result.write(col1[i].replace('\n', '') + '\t' + col2[i])

result.close()