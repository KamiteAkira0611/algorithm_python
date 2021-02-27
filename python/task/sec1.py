"""
数字列Aと数字Bが与えられる。数字列Aの中間の列を足し合わせた数でBに一致するものがあるかどうか調べなさい。

例
A = 7394032 ,    B= 13の時
中間の列94が13なのでtrue
A = 780529423 ,    B= 16の時
足し合わせて16 になる中間の列がないのでfalse
"""

def pulsArr(arr, B):
  answer = 0
  for num in arr:
    answer += int(num)
    print(answer)
    if answer > B: return False
    if answer == B: return True
  return False

def func(A = 7394032, B = 13):
  a_list = list(str(A))
  for i in range(0, len(a_list)):
    arr = a_list[i:len(a_list)]
    isPlesent = pulsArr(arr, B)
    if isPlesent: return True
  
  return False

A = 780529423
B = 16

answer = func(A, B)
print(answer)
