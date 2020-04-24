'''
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
'''
import q20, re

text = q20.getBritishText()

# テンプレート抽出
template = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}$', text, re.M + re.DOTALL)

# キーと値を取得
patterns = re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template[0], re.M + re.DOTALL)

result = {}
for pattern in patterns:
    result[pattern[0]] = re.sub(r'(\'{3}|\'{5})|\[\[|\]\]', '', pattern[1])

print(result)