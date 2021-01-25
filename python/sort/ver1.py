# 選択ソート

def sort(list):
  answer = []
  while range(0, len(list)):
    max, max_i = selectMaxIndex(list)
    answer.insert(0,max)
    del list[max_i]
  
  return answer

def selectMaxIndex(arr):
  max = 0
  index = 0
  max_i = 0
  for num in arr:
    if num > max: 
      max = num
      max_i = index

    index += 1
      
  return max, max_i

origin_list = [38, 14, 33, 25, 31, 23, 29, 6, 46, 32, 50, 3, 10, 36, 17, 17, 14, 13, 35, 22]
# arr = mySort1(origin_list)

arr = sort(origin_list)
print(arr)