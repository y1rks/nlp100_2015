'''
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
'''
import q20, re, requests

text = q20.getBritishText()

# テンプレート抽出
template = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}$', text, re.M + re.DOTALL)

# キーと値を取得
patterns = re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template[0], re.M + re.DOTALL)

result = {}
for pattern in patterns:
    result[pattern[0]] = re.sub(r'(\'{3}|\'{5})|\[\[|\]\]', '', pattern[1])


# ここからAPIリクエスト処理
S = requests.Session()

URL = 'https://ja.wikipedia.org/w/api.php'

PARAMS = {
    'action': 'query',
    'format': 'json',
    'prop': 'imageinfo',
    'titles': 'File:' +  result['国旗画像'],
    'iiprop': 'url'
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

imageUrl = DATA['query']['pages']['-1']['imageinfo'][0]['url']

print(imageUrl)
