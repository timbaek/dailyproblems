import sys

'''
Given an integer array, find the second largest element.


예제)

Input: [10, 5, 4, 3, -1]

Output: 5


Input: [3, 3, 3]

Output: Does not exist.
'''

def solution(arr):
  first, second = -sys.maxsize-1, -sys.maxsize-1
  for x in arr:
    if x > first:
      second = first
      first = x
    elif x < first and x > second:
      second = x
  
  if second == -sys.maxsize-1:
    return 'Does not exist.'
  else:
    return second

print(solution([10, 5, 4, 3, -1]))
print(solution([3,3,3]))
