def febo(max):
  num = 1
  num2 = 1
  for i in range(0, max):
    febo_num = num + num2
    print(febo_num)
    if (i % 2 == 0):
      num = febo_num
    else:
      num2 = febo_num

febo(35)
