'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
from utils import print_matrix

def rotate(matrix):
  start, end = 0, len(matrix) - 1

  def swap(matrix, x1, y1, x2, y2):
    matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
  
  while start < end:
    k = 0
    while start + k < end:
      swap(matrix, start, start+k, end-k, start)
      swap(matrix, end-k, start, end, end-k)
      swap(matrix, end, end-k, start+k, end)
      k+=1
    start += 1
    end -= 1
  
  return matrix

# Test 1
t1_input = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
t1_output = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
assert(t1_output == rotate(t1_input))

# Test 2
t2_input = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
t2_output = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
assert(t2_output == rotate(t2_input))
