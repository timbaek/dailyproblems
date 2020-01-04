"""
Chapter 01 | Problem 07 - Rotate Matrix

Problem Statement:
  Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
  write a method to rotate the image by 90 degrees. Can you do this in place?
"""
import unittest

def rotate_matrix(matrix):
  n = len(matrix)

  for layer in range(0, n // 2):
    first, last = layer, n - layer - 1
    for elem in range(first, last):
      offset = elem - first

      top = matrix[first][elem]
      right = matrix[elem][last]
      bottom = matrix[last][last-offset]
      left = matrix[last-offset][first]

      matrix[first][elem] = left
      matrix[elem][last] = top
      matrix[last][last-offset] = right
      matrix[last-offset][first] = bottom
  
  return matrix

class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ([
      [3,7,2],
      [1,8,4],
      [5,0,6]
    ],[
      [5,1,3],
      [0,8,7],
      [6,4,2]
    ])
  ]

  def test_rotate_matrix(self):
    for [test_matrix, expected] in self.data:
      actual = rotate_matrix(test_matrix)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
