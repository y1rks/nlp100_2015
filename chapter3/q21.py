'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''
import q20, re

text = q20.getBritishText()
patterns = re.findall(r'^\[\[Category.+$', text, flags=re.M)
print(patterns)