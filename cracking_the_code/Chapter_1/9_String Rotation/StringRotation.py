"""
Chapter 01 | Problem 09 - String Rotation

Problem Statement:
  Assume you have amethod isSubstring which checks if one word is a substring of another. 
  Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only 
  one call to isSubstring (e.g.,"waterbottle"is a rotation of "erbottlewat").
"""
import unittest

def is_substrng(string, sub):
  return string.find(sub) != -1

def string_rotation(s1, s2):
  if len(s1) == len(s2) != 0:
    return is_substrng(s2 + s2, s1)
  return False


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ("waterbottle", "erbottlewat", True),
    ("", "", False)
  ]

  def test_string_rotation(self):
    for [test_s1, test_s2, expected] in self.data:
      actual = string_rotation(test_s1, test_s2)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
