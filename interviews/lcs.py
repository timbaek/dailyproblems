'''
Longest Common Prefix

Idea:
  Create a dp table and count if there is a match between characters.
    - If s1_i == s2_i, check the answer in table at (row - 1 , col - 1)
'''

def lcs(s1,s2):
  M, N = len(s1), len(s2)
  table = [[0 for col in range(N+1)] for row in range(M+1)]
  
  for row in range(1,M+1):
    for col in range(1,N+1):
      table[row][col] = max( table[row][col-1], table[row-1][col] )
      if s1[row-1] == s2[col-1]:
        table[row][col] = max( table[row][col], table[row-1][col-1] + 1 )

  return table[M][N]

# Test 1
assert(4 == lcs("GXTXAYB", "AGGTAB"))
