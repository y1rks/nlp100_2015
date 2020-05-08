'''
36. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''
import q30
import matplotlib.pyplot as plt

data = q30.mapper()
words = {}

for word in data:
    if word['surface'] in words:
        words[word['surface']] += 1
    else:
        words[word['surface']] = 1

result = sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]

x = []
y = []

for word in result:
    x.append(word[0])
    y.append(word[1])

plt.bar(x, y)
plt.show()