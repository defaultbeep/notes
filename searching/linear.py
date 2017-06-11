# insertion sort with linear search

nums = [1,4,2,-4,6,9,0,2,3,3,10,7,2,1,1]

def insertion(list):
  for cp in range(1, len(list)):
    for lb in range(cp - 1, -1, -1):
      if(list[lb + 1] < list[lb]):
        swap = list[lb]
        list[lb] = list[lb + 1]
        list[lb + 1] = swap
  return list

def linear(list, item):
  for li in range(0, len(list)):
    if(list[li] == item):
      return li
  return -1

sorted_nums = insertion(nums)
print linear(nums, 10)

