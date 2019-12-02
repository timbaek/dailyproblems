'''
문자열 배열(string array)이 주어지면, 제일 긴 공통된 접두사(prefix)의 길이를 찾으시오.

Given an array of strings, find the longest common prefix of all strings.

예제)
Input: ["apple", "apps", "ape"]
Output: 2 // "ap"


Input: ["hawaii", "happy"]
Output: 2 // "ha"


Input: ["dog", "dogs", "doge"]
Output: 3 // "dog"
'''
import sys

def containsPrefix(strings, s, left, right):
  for string in strings:
    for i in range(left,right+1):
      if string[i] != s[i]: return False
  return True

def findMinLength(strings):
  min_len = sys.maxsize
  for s in strings:
    if len(s) < min_len: min_len = len(s)

  return min_len

def solution(strings):
  min_len = findMinLength(strings)
  prefix = ""

  left, right = 0, min_len - 1
  while left <= right:
    mid = left + (right - left) // 2

    if containsPrefix(strings, strings[0], left, mid):
      prefix += strings[0][left:mid+1]

      left = mid + 1
    else:
      right = mid - 1
  return len(prefix)


# Test 1
assert(2 == solution(["apple", "apps", "ape"]))
# Test 2
assert(2 == solution(["hawaii", "happy"]))
# Test 3
assert(3 == solution(["dog", "dogs", "doge"]))
