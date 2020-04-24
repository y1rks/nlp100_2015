'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
'''
import q20, re

text = q20.getBritishText()

# テンプレート抽出
template = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}$', text, re.M + re.DOTALL)

# キーと値を取得
patterns = re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template[0], re.M + re.DOTALL)

result = {}
for pattern in patterns:
    result[pattern[0]] = re.sub(r'\'{2,3}|\'{5}', '', pattern[1])

print(result)