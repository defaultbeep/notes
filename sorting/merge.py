# merge

def merge(left, right):

  result = []

  while len(left) > 0 and len(right) > 0:

    if(left[0] < right[0]):
      result.append(left[0])
      left.remove(left[0])
    else:
      result.append(right[0])
      right.remove(right[0])

  while len(left) == 0 and len(right) > 0:

    result.append(right[0])
    right.remove(right[0])

  return result


def mergesort(list):
	
  if len(list) <= 1:
    return list
	
  middle = int(len(list) / 2)
  left = mergesort(list[:middle])
  right = mergesort(list[middle:])
  return merge(left, right)

print mergesort([2,1,3,6,3,5,2,1,5,6,7,7,0,-3,7713])

