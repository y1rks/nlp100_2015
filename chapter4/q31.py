'''
31. 動詞
動詞の表層形をすべて抽出せよ．
'''
import q30

for word in q30.mapper():
    print(word['surface'])