'''
정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오.

단, 시간복잡도 O(n) 여야 합니다.

Given an array of integers and a target integer, find two indexes of the array element that sums to the target number.


예제)

Input: [2, 5, 6, 1, 10], 타겟 8
Output: [0, 2] // 배열[0] + 배열[2] = 8

Input: [2, 5, 6, 1, 10], 타겟 6
Output: [1, 3]

'''

def solution(arr, target):
  s = {}

  result = []
  for i in range(0,len(arr)):
    temp = target - arr[i]
    if temp in s:
      result.append(i)
      result.append(s.get(temp))
      break
    s[arr[i]] = i
  return result

print(solution([2, 5, 6, 1, 10], 8))
