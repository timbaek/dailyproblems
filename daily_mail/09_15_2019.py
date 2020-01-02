'''
정렬(sort)된 정수 배열과 정수 n이 주어지면, 배열안에 n이 있는지 체크하시오. 시간복잡도를 최대한 최적화하시오.


Given a sorted integer array and an integer N, check if N exists in the array.
 

예제)

Input: [1, 2, 3, 7, 10], 7
Output: true


Input: [-5, -3, 0, 1], 0
Output: true


Input: [1, 4, 5, 6, 8, 9], 10
Output: false
'''

def bsearch_recursive(arr, left, right, n):
  if left > right:
    return False

  mid = left + (right - left) // 2

  if n == arr[mid]: return True
  elif n < arr[mid]:
    return bsearch_recursive(arr, left, mid - 1, n)
  else:
    return bsearch_recursive(arr, mid + 1, right, n)

def bsearch_iterative(arr, left, right, n):
  while left <= right:
    mid = left + (right - left) // 2

    if n == arr[mid]: return True
    elif n < arr[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return False

def solution(arr, n):
  # return bsearch_iterative(arr, 0, len(arr) - 1, n)
  return bsearch_recursive(arr, 0, len(arr) - 1, n)

# Test 1
assert(True == solution([1, 2, 3, 7, 10], 7))
# Test 2
assert(True == solution([-5, -3, 0, 1], 0))
# Test 3
assert(False == solution([1, 4, 5, 6, 8, 9], 10))
# Test 4
assert(True == solution([1, 4, 5, 6, 8, 9], 9))
# Test 5
assert(True == solution([1, 4, 5, 6, 8, 9], 1))
