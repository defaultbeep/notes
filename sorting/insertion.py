# insertion sort

test_1 = []
test_2 = [1]
test_3 = [1,2,3,4,5]
test_4 = [1,4,2,-4,6,9,0,2,3,3,10,7,2,1,1]
test_5 = [-1,-5,-6,70,40,34.9]

def insertion(nums):
  for cp in range(1, len(nums)):
    for lb in range(cp - 1, -1, -1):
      if(nums[lb + 1] < nums[lb]):
        swap = nums[lb]
        nums[lb] = nums[lb + 1]
        nums[lb + 1] = swap
  return nums

print insertion(test_1)
print insertion(test_2)
print insertion(test_3)
print insertion(test_4)
print insertion(test_5)
