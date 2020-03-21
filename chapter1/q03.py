'''
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ
'''

strs = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'.replace(',', '').replace('.', '').split(' ')
counts = []

for str in strs:
  counts.append(len(str))

print(counts)