'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
'''
import q20, re

text = q20.getBritishText()

# テンプレート抽出
template = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}$', text, re.M + re.DOTALL)

# キーと値を取得
patterns = re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template[0], re.M + re.DOTALL)

result = {}
for pattern in patterns:
    result[pattern[0]] = re.sub(r'(\'{3}|\'{5})|\[\[|\]\]|(?s)\<ref.*(\/\>|ref\>)|\<br.*\/\>', '', pattern[1])


print(result)