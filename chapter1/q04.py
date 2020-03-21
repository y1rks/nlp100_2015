'''
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

strs = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'.replace(',', '').replace('.', '').split(' ')

oneWordList = [1, 5, 6, 7, 8, 9, 15, 16, 19]

result = {}

for i in range(len(strs)):
  str = strs[i]
  if (i + 1 in oneWordList):
    result[str[:1]] = i + 1
  else:
    result[str[:2]] = i + 1

print(result)