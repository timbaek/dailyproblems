'''
Given an integer, check if it is a palindrome.

예제)
Input: 12345
Output: False

Input: -101
Output: False

Input: 11111
Output: True

Input: 12421
Output: True
'''

def solution(x):
  if x < 0:
    return False

  original_x = x

  result = 0
  while x != 0:
    pop = x % 10
    x = x // 10
    result = result * 10 + pop
  
  return result == original_x

print(solution(12345))
print(solution(-101))
print(solution(11111))
print(solution(12421))
