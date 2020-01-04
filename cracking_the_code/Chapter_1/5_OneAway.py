"""
Chapter 01 | Problem 05 - One Away

Problem Statement:
  There are three types of edits that can be performed on strings: insert a character, 
  remove a character, or replace a character. Given two strings, write a function to 
  check if they are one edit (or zero edits) away.

Examples:
  pale, ple => True
  pales, pale => True
  pale, bale => True
  pale, bake => False
"""
import unittest

def one_away(s1, s2):
  '''Check if a string can converted to another string with a single edit'''
  if len(s1) == len(s2):
    return one_edit_replace(s1, s2)
  elif len(s1) + 1 == len(s2):
    return one_edit_insert(s1, s2)
  elif len(s1) - 1 == len(s2):
    return one_edit_insert(s2, s1)
  return False

def one_edit_replace(s1, s2):
  edited = False
  for c1, c2 in zip(s1, s2):
    if c1 != c2:
      if edited:
        return False
      edited = True
  return True

def one_edit_insert(s1, s2):
  edited = False
  i, j = 0, 0
  while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:
      if edited:
        return False
      edited = True
      j += 1
    else:
      i += 1
      j += 1
  return True


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ("pale", "ple", True),
    ("pales", "pale", True),
    ("pale", "bale", True),
    ("pale", "bake", False),
    ("pale", "bales", False),
    ("p", "", True),
    ("", "bake", False),
    ("pr", "r", True),
    ("pr", "rp", False),
    ("brrr", "brrss", False),
    ("abc", "acs", False),
    ("aple", "aple",True)
  ]

  def test_one_away(self):
    for [test_s1, test_s2, expected] in self.data:
      actual = one_away(test_s1, test_s2)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
