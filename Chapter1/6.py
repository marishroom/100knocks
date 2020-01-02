#"paraparaparadise"と"paragraph"のbi-gramをXとYの集合として求める.
#XとYの和集合，積集合，差集合を求めよ.
#"se"というbi-gramがXとYにあるかどうか調査.

def n_gram(a, n):
  result = []

  for i in range(0, len(a) - n + 1):
    result.append(a[i:i + n])

  return result

#集合作成
#set型　重複がなく，順序がない要素
x = set(n_gram("paraparaparadise", 2))
print("X:" + str(x))
y = set(n_gram("paragraph", 2))
print("Y:" + str(y))

#和集合　両方の集合のすべての要素
c = x | y
print("和集合:" + str(c))

#積集合　両方の集合にある要素の集まり
d = x & y
print("積集合:" + str(d))

#差集合　AからAとBの積集合を削除した要素の集まり
e = x - y
print("差集合:" + str(e))

#"se"の有無
print("Xにseがあるか:" + str("se" in x))
print("Yにseがあるか:" + str("se" in y))

