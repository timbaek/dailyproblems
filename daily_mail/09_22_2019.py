'''
정수 배열과 정수 k가 주어지면 모든 원소를 k칸씩 앞으로 옮기시오.


Given an array and an integer K, shift all elements in the array K times.


Input: [1, 2, 3, 4, 5], k = 2
Output: [3, 4, 5, 1, 2]


Input: [0, 1, 2, 3, 4], k = 1
Output: [1, 2, 3, 4, 0]

시간복잡도와 공간복잡도를 최대한 최적화 하시오.
'''

# In Python, we can get subset of array so it is easy to do
#  e.g arr[k:len(arr)] + arr[0:k]


def solution(arr, k):
  n = len(arr)
  k %= n

  if k == n: return arr
  else:
    j = n - k
    prev = temp = arr[0]

    while j != 0:
      temp = arr[j]
      arr[j] = prev
      j = j - k if j - k >= 0 else n + j - k
      prev = temp
    arr[j] = prev

  return arr


# Test 1
assert([3, 4, 5, 1, 2] == solution([1, 2, 3, 4, 5], 2))
# Test 2
assert([1, 2, 3, 4, 0] == solution([0, 1, 2, 3, 4], 1))
