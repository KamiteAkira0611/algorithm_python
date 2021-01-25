# 挿入ソート
def sort(list):
  answer = []
  for num in list:
    index = searchIndex(answer, num)
    answer.insert(index, num)
  return answer

def searchIndex(arr, num):
  i = 0
  for a_num in arr:
    if num < a_num: break
    i += 1

  return i

origin_list = [38, 14, 33, 25, 31, 23, 29, 6, 46, 32, 50, 3, 10, 36, 17, 17, 14, 13, 35, 22]
a = sort(origin_list)
print(a)