'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
'''

import q20, re

text = q20.getBritishText()
patterns = re.findall(r'^(=+)(.+?)=+$', text, flags=re.M)
for p in patterns:
    print(p[1] + ' ' + str(len(p[0]) - 1))