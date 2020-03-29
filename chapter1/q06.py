'''
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''

str1 = 'paraparaparadise'
str2 = 'paragraph'
X = set()
Y = set()

for i in range(len(str1) - 1):
  X.add(str1[i:i+2])

for i in range(len(str2) - 1):
  Y.add(str2[i:i+2])

union = X | Y
intersection = X & Y
difference1 = X - Y
difference2 = Y - X
isExistInX = 'se' in X
isExistInY = 'se' in Y

print(union)
print(intersection)
print(difference1)
print(difference2)
print(isExistInX)
print(isExistInY)
