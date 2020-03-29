'''
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''

def cipher(doc: str):
  result = ''
  for char in doc:
    if char.islower():
      result += chr(219 - ord(char))
    else:
      result += char
  return result

doc = 'There are 8000000 Gods in Japan.'

print(cipher(doc))
