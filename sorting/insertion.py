# insertion sort

nums = [1,4,2,-4, 6,9,0,2,3,3,10,7,2,1,1]

for cp in range(1, len(nums)):
  for lb in range(cp - 1, -1, -1):
    if(nums[lb + 1] < nums[lb]):
      swap = nums[lb]
      nums[lb] = nums[lb + 1]
      nums[lb + 1] = swap

print nums

