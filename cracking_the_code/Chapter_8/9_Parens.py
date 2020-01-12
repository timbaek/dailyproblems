"""
Chapter 08 | Problem 09 - Parenthesis

Problem Statement:
  Implement an algorithm to print all valid (e.g., properly opened and closed)
  combinations of n pairs of parentheses.

Example
  Input: 3
  Output: ((())), (()()), (())(), ()(()), ()()()
"""

def build_parentheses(paranthesis, left, right, result):
  if left == 0 and right == 0:
    result.append(paranthesis)
    return

  if left > 0:
    build_parentheses(paranthesis + '(', left - 1, right, result)

  if left < right:
    build_parentheses(paranthesis + ')', left, right - 1, result)


def parens(n):
  result = []
  build_parentheses('', n, n, result)
  print(result)


# Tests
parens(3)