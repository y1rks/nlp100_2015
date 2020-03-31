'''
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

fileName = 'hightemp.txt'

with open(fileName) as f:
  print(len(f.readlines()))