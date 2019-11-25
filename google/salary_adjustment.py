'''

Give an array of salaries. The total salary has a budget. At the beginning, the total salary of employees is
larger than the budget. It is required to find the number k, and reduce all the salaries larger than k to k,
such that the total salary is exactly equal to the budget.

Example 1:

Input: salaries = [100, 300, 200, 400], budget = 800
Output: 250

Explanation: k should be 250, so the total salary after the reduction 100 + 250 + 200 + 250 is exactly equal to 800.
You can assume that solution always exists.

'''
def solution(salaries, budget):
  if len(salaries) == 1:
    return budget

  total_sum = 0
  for x in salaries:
    total_sum += x

  sorted_salaries = sorted(salaries)

  k, i = budget, len(sorted_salaries) - 1
  while i > 0:
    total_sum -= sorted_salaries[i]
    k = (budget - total_sum) // (len(sorted_salaries) - i)

    if k > sorted_salaries[i-1]:
      break

    i -= 1

  return k

# Test 1
assert(250 == solution([100, 300, 200, 400], 800))
# Test 1
assert(250 == solution([100, 300, 200, 400], 600))
