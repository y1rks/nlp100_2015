'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''
import q20, re

text = q20.getBritishText()

patterns = re.findall(r'(?:ファイル|File):(.+?)\|', text)
print(patterns)