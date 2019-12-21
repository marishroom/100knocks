#"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# 上記の文を単語に分解
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出す
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
result = {}
#{}は辞書
firstNum = (1, 5, 6, 7, 8, 9, 15, 16, 19)

words = str.split(" ")
for (num, word) in enumerate(words,1):
  #enumerate　インデックス番号, 要素の順に2つを取得する関数
  if num in firstNum:
    result[word[0:1]] = num
  else:
    result[word[0:2]] = num

print(result)
