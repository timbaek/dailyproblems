"""
Chapter 08 | Problem 01 - Triple Step

Problem Statement:
  A child is running up a staircase with n steps and can hop either 1 step, 2 steps, 
  or 3 steps at a time. Implement a method to count how many possible ways the child 
  can run up the stairs.
"""

def count_ways(n, memo):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif memo[n] > -1:
    return memo[n]
  else:
    memo[n] = count_ways(n-1, memo) + count_ways(n-2, memo) + count_ways(n-3, memo)
    return memo[n]


def triple_step(n):
  memo = [-1] * (n + 1)
  count_ways(n,memo)
  print(memo)
  return memo

  


# Tests
triple_step(8)