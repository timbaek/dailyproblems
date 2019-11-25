
def maxArea(height):
  i,j = 0, len(height) - 1

  max_area = 0
  while i < j:
    max_area = max(max_area, min(height[i], height[j]) * (j - i))

    if height[i] < height[j]:
      i += 1
    else:
      j -= 1
  
  return max_area

# Test 1
assert(49 == maxArea([1,8,6,2,5,4,8,3,7]))
