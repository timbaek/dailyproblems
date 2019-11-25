'''
Longest Palindromic Substring

Idea:
  Create dp table
    - Fill out length of 1 and 2, which is the diagnols
    - If boundary characters are equal, check the non-boundary
'''
from utils import print_matrix

def lps(s):
  M, N = len(s), len(s)
  table = [[0 for col in range(N)] for row in range(M)]

  # Fill diagonals of length 1
  for i in range(M):
    table[i][i] = 1

  max_len,left,right = 1,0,0
  # Fill diagonals of length 2
  for i in range(M-1):
    if s[i] == s[i+1]:
      table[i][i+1] = 1
      left, right = i, i + 1
      max_len = 2

  row, col_base = 0, 0
  while col_base < N - 2:
    col = col_base + row + 2
    if s[row] == s[col] and table[row+1][col-1] == 1:
      table[row][col] = 1

      if col - row + 1 > max_len:
        max_len = col - row + 1
        left,right = row, col
    else:
      table[row][col] = 0
    
    if col == M - 1:
      row = 0
      col_base += 1
    else:
      row += 1

  return s[left:right+1]

# Test 1
assert("abcba" == lps("abcba"))
# Test 2
assert("aabbaa" == lps("aaaabbaa"))
# Test 3
assert("bab" == lps("babad"))

