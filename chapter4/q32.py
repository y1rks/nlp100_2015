'''
32. 動詞の原形
動詞の原形をすべて抽出せよ．
'''
import q30

for line in q30.mapper():
    print(line['base'])