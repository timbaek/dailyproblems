'''
정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.

Given an integer array, move all the 0s to the right of the array without changing the order of non-zero elements.

예제)

Input: [0, 5, 0, 3, -1]

Output: [5, 3, -1, 0, 0]


Input: [3, 0, 3]

Output: [3, 3, 0]
'''


def solution(arr):
  count = 0

  for i in range(0,len(arr)):
    if not arr[i] == 0:
      arr[count] = arr[i]
      count += 1

  while count < len(arr):
    arr[count] = 0
    count += 1

  return arr

print(solution([0, 5, 0, 3, -1]))
print(solution([3, 0, 3]))
print(solution([1, 2, 0, 4, 3, 0, 5, 0]))
print(solution([1, 2, 0, 0, 0, 3, 6]))
