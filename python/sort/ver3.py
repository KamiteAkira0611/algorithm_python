# バブルソート
def sort(list):
  arr = bubble(list, len(list))
  return arr

def bubble(arr, max):
  for i in range(0,max - 1):
    if arr[i] > arr[i + 1]: 
      arr[i], arr[i + 1] = arr[i + 1], arr[i]

  print(arr)
  if max - 1 == 0:
    return arr

  return bubble(arr, max - 1)


l = [38, 14, 33, 25, 31, 23, 29, 6, 46, 32, 50, 3, 10, 36, 17, 17, 14, 13, 35, 1]
arr = sort(l)
# print(arr)