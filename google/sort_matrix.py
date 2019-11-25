'''

Given a 2D array where all rows are sorted, write a program to sort the array

'''
import sys


def find_min(matrix, col_ptrs, row_start):
  min_index, min_num = 0, sys.maxsize
  for r in range(len(matrix)):
    col_start = col_ptrs[r]
    if col_start < len(matrix[0]) and matrix[r][col_start] < min_num:
      min_num = matrix[r][col_start]
      min_index = r
  
  return min_index

def solution(matrix):
  N, M = len(matrix), len(matrix[0])

  sorted_matrix = [[0 for _ in range(M)] for _ in range(N)]
  col_ptrs = [0 for _ in range(N)]

  for row in range(N):
    for col in range(M):
      min_row = find_min(matrix, col_ptrs, row)

      sorted_matrix[row][col] = matrix[min_row][col_ptrs[min_row]]

      # update col_ptrs
      if col_ptrs[min_row] <= N:
        col_ptrs[min_row] += 1

  return sorted_matrix


from queue import PriorityQueue

def sort_usingpq(matrix):
  q = PriorityQueue()
  col_ptrs = {}

  for i in range(len(matrix)):
    q.put((matrix[i][0],(i,0)))
    col_ptrs[i] = 0

  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      min_val, rowcol = q.get()

      q.put((matrix[row][col], (row,col)))
      col_ptrs[rowcol[0]] = rowcol[1] + 1
      
      matrix[row][col] = min_val
      
      q.put((matrix[rowcol[0]][rowcol[1]], (rowcol[0], rowcol[1])))
  
  print(matrix)
  return matrix





# Test 1
t1_input = [[ 5, 12, 17, 21, 23],
            [ 1,  2,  4,  6,  8],
            [12, 14, 18, 19, 27],
            [ 3,  7,  9, 15, 25]]
t1_output = [[ 1,  2,  3,  4,  5],
             [ 6,  7,  8,  9, 12],
             [12, 14, 15, 17, 18],
             [19, 21, 23, 25, 27]]
assert(t1_output == solution(t1_input))
assert(t1_output == sort_usingpq(t1_input))