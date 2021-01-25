import random

def create_num_list(min, max, length):
  
  arr = []
  while len(arr) != length:
    arr.append(random.randint(min, max))

  return arr

arr = create_num_list(1, 50, 20)
print(arr)
