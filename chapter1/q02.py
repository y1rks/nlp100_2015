'''
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''

str1 = 'パトカー'
str2 = 'タクシー'
result = ''

for i in range(len(str1)):
  result += str1[i] + str2[i]

print(result)