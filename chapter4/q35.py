'''
35. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''
import q30

data = q30.mapper()
words = {}

for word in data:
    if word['surface'] in words:
        words[word['surface']] += 1
    else:
        words[word['surface']] = 1

result = sorted(words.items(), key=lambda x: x[1], reverse=True)

print(result)