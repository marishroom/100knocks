#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
#さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

from string  import Template

def format(a, b, c):
  x = Template("$hourの時の$targetは$value")
  #テンプレート文字列は$に基づいた置換をサポートする

  return x.substitute(hour = a, target = b, value = c)
  #substitute テンプレート置換を行い、新たな文字列を生成して返

a = 12
b = "気温"
c = 22.4
print(format(a, b, c))
