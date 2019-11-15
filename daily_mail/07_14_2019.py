'''
정수로된 배열이 주어지면, 각 원소가 자신을 뺀 나머지 원소들의 곱셈이 되게하라.

단, 나누기 사용 금지, O(n) 시간복잡도


Given an integer array, make each element, a product of all element values without itself.

예제)

Input: [1, 2, 3, 4, 5]
Output: [120, 60, 40, 30, 24]
'''

import math

def solution(lst):
  sum = 0
  for x in lst:
    sum += math.log10(x)

  prods = []
  for x in lst:
    prods.append(int(math.ceil((pow(10, sum - math.log10(x))))))
  
  return prods

# Test 1
assert([120, 60, 40, 30, 24] == solution([1, 2, 3, 4, 5]))
# Test 2
