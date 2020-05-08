'''
37. 「猫」と共起頻度の高い上位10語
「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
→ 文単位で共起を計算した
'''
import q30
import matplotlib.pyplot as plt

data = q30.mapper()
coWords = {}
words = {}
catFlag = False
for word in data:
    if word['surface'] == '。':
        # 文の終わり
        if catFlag:
            for key in words:
                if key in coWords:
                    coWords[key] += words[key]
                else:
                    coWords[key] = words[key]
        words = {}
        catFlag = False
        continue

    if word['surface'] == '猫':
        catFlag = True
        continue

    if word['surface'] in words:
        words[word['surface']] += 1
    else:
        words[word['surface']] = 1


result = sorted(coWords.items(), key=lambda x: x[1], reverse=True)[:10]

x = []
y = []

for word in result:
    x.append(word[0])
    y.append(word[1])

plt.bar(x, y)
plt.show()