#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成
#この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

#n-gramとは(一応)
#任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法

def n_gram(x, n):
  result = []

  #range関数は指定した長さの、連続した整数のリストを自動で生成する関数
  for i in range(0, len(x) - n + 1):
  #for 変数 in range([始まりの数値,] 最後の数値[, 増加する量]):
    result.append(x[i:i + n])
  return result

x = "I am an NLPer"
xwords = x.split(" ")

#単語bi-gram
result = n_gram(xwords, 2)
print(result)

#文字bi-gram
result = n_gram(x, 2)
print(result)