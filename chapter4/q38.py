'''
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
'''
import q30
import numpy as np
import matplotlib.pyplot as plt

data = q30.mapper()
words = {}

for word in data:
    if word['surface'] in words:
        words[word['surface']] += 1
    else:
        words[word['surface']] = 1

freqs = []

for key in words:
    freqs.append(words[key])

plt.hist(freqs, bins=50, range=(1, 50))
plt.show()