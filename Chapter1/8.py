#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(x):
  result = ""

  for c in x:
    if c.islower():
      result += chr(219 - ord(c))
      #chr関数　ASCIIコードをASCII文字に変更
      #ord関数　ASCII文字をASCIIコードとして返す
    else:
      result += c
    
  return result


#文字列の入力
x = input("文字列を入力してください--> ")

#暗号化
result = cipher(x)
print("暗号化:" + result)

#復号化
result2 = cipher(result)
print("復号化:" + result2)

#もとに戻ってるかチェック
if result2 != x:
  print("復号失敗;;;")
else:
  print("復号完了b")

