'''
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''

def getWordNGram(n: int, sequence: []):
  result = []
  for i in range(len(sequence) - 1):
    result.append({sequence[i]: sequence[i + 1]})
  return result

def getCharNGram(n: int, string: str):
  result = []
  for i in range(len(string) - 1):
    result.append(string[i] + string[i + 1])
  return result


print(getWordNGram(2, 'I am an NLPer'.split(' ')))
print(getCharNGram(2, 'I am an NLPer'))