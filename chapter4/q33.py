'''
33. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
'''

import q30

data = q30.mapper()
lastIndex = len(data) - 1
result = []
for i in range(lastIndex + 1):
    if data[i]['surface'] == 'の' and i != 0 and i != lastIndex:
        if data[i - 1]['pos'] == '名詞' and data[i + 1]['pos'] == '名詞':
            result.append(data[i - 1]['surface'] + data[i]['surface'] + data[i + 1]['surface'])

print(result)