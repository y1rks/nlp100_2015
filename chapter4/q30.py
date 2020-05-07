'''
第4章: 形態素解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．

MeCabの出力フォーマット
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
'''
import re

def mapper():
    fileName = 'neko.txt.mecab'
    result = []

    with open(fileName, encoding='utf-8') as f:
        for line in f.readlines():
            patterns = re.findall(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?).*$', line)
            if len(patterns) != 0:
                wordAttribute = {}
                wordAttribute['surface'] = patterns[0][0]
                wordAttribute['base'] = patterns[0][7]
                wordAttribute['pos'] = patterns[0][1]
                wordAttribute['pos1'] = patterns[0][2]
                result.append(wordAttribute)
    
    return result

if __name__ == '__main__':
    print(mapper())