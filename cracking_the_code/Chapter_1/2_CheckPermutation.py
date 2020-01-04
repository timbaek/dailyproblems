"""
Chapter 01 | Problem 02 - Check Permutation

Problem Statement:
  Given two strings, write a method to decide if one is a permutation of the other.

Examples:
  abcc, cacb => True
  canada, danacc => False

1) Sort => O(n * logN)
2) Hashmap, count characters => O(n) runtime, O(n) space
"""
import unittest

def check_permutation(s1, s2):
  character_counter = {}
  if len(s1) != len(s2): return False

  for c in s1:
    character_counter[c] = character_counter.get(c,0) + 1
  for c in s2:
    character_counter[c] = character_counter.get(c,0) - 1
  for v in character_counter.values():
    if v != 0: return False
  
  return True


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ("abcc", "cacb", True),
    ("abcc", "cacbe", False),
    ("abcc", "caab", False)
  ]

  def test_check_permutation(self):
    for [test_s1, test_s2, expected] in self.data:
      actual = check_permutation(test_s1, test_s2)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()  
