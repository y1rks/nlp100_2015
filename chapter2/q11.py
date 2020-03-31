'''
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
fileName = 'hightemp.txt'

str = ''
with open(fileName) as f:
  str = f.read().replace('\t', ' ')

print(str)
