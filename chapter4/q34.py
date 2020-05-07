'''
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

import q30

data = q30.mapper()
result = []

noneString = ''
noneNumber = 0

for word in data:
    if word['pos'] == '名詞':
        noneString += word['surface']
        noneNumber += 1
        continue

    if noneNumber >= 2:
        result.append(noneString)

    noneString = ''
    noneNumber = 0

if noneNumber >= 2:
    result.append(noneString)

print(result)