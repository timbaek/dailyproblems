'''
Given an integer array and integer N, find the Nth largest element in the array.

예제)

Input: [-1, 3, -1, 5, 4], 2
Output: 4


Input: [2, 4, -2, -3, 8], 1
Output: 8


Input: [-5, -3, 1], 3
Output: -5
'''
import sys

def solution(nums, n):
  if n == len(nums):
    return min(nums)

  max_nums = [-sys.maxsize-1] * n

  for x in nums:
    i = 0
    while i < n:
      if x > max_nums[i]:
        max_nums = max_nums[0:i] + [x] + max_nums[i:n]
        break
      i += 1

  return max_nums[n-1]

# Test 1
assert(4 == solution([-1, 3, -1, 5, 4], 2))
# Test 2
assert(8 == solution([2, 4, -2, -3, 8], 1))
# Test 3
assert(-5 == solution([-5, -3, 1], 3))
