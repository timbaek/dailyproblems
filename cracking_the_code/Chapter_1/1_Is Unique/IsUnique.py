"""
Chapter 01 | Problem 01 - Is Unique

Problem Statement:
  Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?

Examples:
  yolo => False
  rad  => True
  yOlo => True

1) Brute Force => O(n^2)
2) Sort First, then walk thorugh => O(n * logN)
3) Set/Hashmap => O(n) runtime, O(c) space
4) Boolean Array => O(n) runtime, O(1) space

"""
import unittest

def is_unique(s):
  if len(s) > 128:
    return False

  arr = [False] * 128
  for c in s:
    index = ord(c)
    if arr[index]:
      return False
    arr[index] = True
  return True


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ("yolo", False),
    ("rad", True),
    ("yOlo", True)
  ]

  def test_is_unique(self):
    for [test_s, expected] in self.data:
      actual = is_unique(test_s)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
