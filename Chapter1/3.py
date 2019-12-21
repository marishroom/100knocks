#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# 上記の文を単語に分解
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import collections

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result =[]

words = str.split(" ")
for word in words:
  count = 0
  for char in word:
    if char.isalpha:
      count += 1
  result.append(count)

print(result)
