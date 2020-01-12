"""
Chapter 08 | Problem 07 & 08 - Permutations

Problem Statement:
  1) Write a method to compute all permutations of a string of unique characters.
  2) Write a method to compute all permutations of a string whose characters 
     are not necessarily unique. The list of permutations should not have duplicates.
"""

def find_permutation_without_dups(s, result, permutation, visited):
  if len(s) == len(permutation):
    result.append(permutation)
    return

  for c in s:
    if c not in visited:
      visited.add(c)
      permutation += c
      find_permutation_without_dups(s, result, permutation, visited)
      permutation = permutation[:-1]
      visited.remove(c)
      
def permutation_without_dups(s):
  result, permutation = [], ''
  visited = set()
  find_permutation_without_dups(s, result, permutation, visited)
  print(result)

def find_permutation_with_dups(table, prefix, remaining, result):
  if remaining <= 0:
    result.append(prefix)
    return
  
  for c in table:
    count = table.get(c)
    if count > 0:
      table[c] -= 1
      find_permutation_with_dups(table, prefix + c, remaining - 1, result)
      table[c] = count

def permutation_with_dups(s):
  # Build frequency table
  table = {}
  for c in s:
    if c not in table:
      table[c] = 1
    # If I don't want to print duplicate characters,
    # do not increment freq
    table[c] += 1

  # result, remaining = [], len(table)
  result, remaining = [], len(s)
  find_permutation_with_dups(table, '', remaining, result)
  print(result)


# Tests
# permutation_without_dups('sat')
permutation_with_dups('sast')
