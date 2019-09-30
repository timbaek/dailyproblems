'''
Given an integer N, find the number of possible balanced parentheses with N opening and closing brackets.

예제)

Input: 1
Output: ["()"]

Input: 2
Output: ["(())", "()()"]

Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]
'''

def parentheses_builder(s,left,right,result):
  if left == 0 and right == 0:
    result.append(s)
    return
  
  if left > 0:
    parentheses_builder(s + "(", left - 1, right, result)
  
  if left < right:
    parentheses_builder(s + ")", left, right - 1, result)

def solution(n):
  result = []
  parentheses_builder("", n, n, result)
  return result

print(solution(1))
print(solution(2))
print(solution(3))
