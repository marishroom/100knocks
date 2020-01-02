#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする.
#適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

def Typoglycemia(x):
  result = []

  for word in x.split(" "):
    if len(word) <= 4:
      result.append(word)
      print("4文字以下は変換されません")

    else:
      targetList = list(word[1:-1])
      random.shuffle(targetList)
      result.append(word[0] + "".join(targetList) + word[-1])
    
  return " ".join(result)

#文字列の入力
x = input('文字列を入力してください--> ')

#結果
result = Typoglycemia(x)
print("結果:" + result)
