'''
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
'''

import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def convertWord(word: str):
  wordLength = len(word)

  if wordLength <= 4:
    return word

  convertedWord = word[0]
  mediumWord = [char for char in word[1:wordLength - 1]]
  while len(mediumWord) > 0:
    choice = random.choice(mediumWord)
    mediumWord.remove(choice)
    convertedWord += choice

  return convertedWord + word[wordLength - 1]


def convertSentence(str: str):
  convertedSentence = ''
  for word in str.split(' '):
    convertedSentence += convertWord(word) + ' '
  return convertedSentence.strip(' ')


print(convertSentence(str))