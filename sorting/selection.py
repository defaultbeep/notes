# selection sort

test_1 = []
test_2 = [1]
test_3 = [7,12,9,10,11]
test_4 = [1,4,2,-4,6,9,0,2,3,3,10,7,2,1,1]
test_5 = [-1,-5,-6,70,40,349]

def selection(nums):
  for cp in range(0, len(nums)):
    cm = cp
    for lk in range(cp + 1, len(nums)):
      if(nums[lk] < nums[cm]):
        cm = lk
    swap = nums[cp]
    nums[cp] = nums[cm]
    nums[cm] = swap
  return nums

print selection(test_1)
print selection(test_2)
print selection(test_3)
print selection(test_4)
print selection(test_3)
