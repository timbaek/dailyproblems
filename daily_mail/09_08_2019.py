'''
O(n log n)시간 복잡도를 가진 정수 배열 정렬 알고리즘을 구현하시오.

Implement an O(n log n) time complexity sorting algorithm.
 

예제)

Input: [3, 1, 5, 6]
Output: [1, 3, 5, 6]
'''

def solution(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    solution(L)
    solution(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1
    
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

    return arr

# Test 1
assert([1,3,5,6] == solution([3,1,5,6]))
