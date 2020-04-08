'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''
import q20, re

text = q20.getBritishText()
patterns = re.findall(r'^\[\[Category:(.+?)(?:\|.*)?\]\]$', text, flags=re.M)
print(patterns)
