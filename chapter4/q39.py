'''
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
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

result = sorted(words.items(), key=lambda x: x[1], reverse=True)

x = []
y = []

count = 1
for word in result:
    x.append(count)
    y.append(word[1])
    count += 1

plt.plot(x, y)
plt.xscale('log')
plt.yscale('log')
plt.show()