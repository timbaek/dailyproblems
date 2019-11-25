
def backtrack(result, nums, permutation, visited):
  if len(nums) == len(permutation):
    result.append(permutation[:])
    return
  
  for num in nums:
    if num not in visited:
      visited.add(num)
      permutation.append(num)
      backtrack(result, nums, permutation, visited)
      visited.remove(num)
      permutation.pop()

def permute(nums):
  result = []
  permutation = []
  visited = set()
  backtrack(result, nums, permutation, visited)
  return result

# Test 1
t1_input = [1,2,3]
t1_output = [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
assert(t1_output == permute(t1_input))
