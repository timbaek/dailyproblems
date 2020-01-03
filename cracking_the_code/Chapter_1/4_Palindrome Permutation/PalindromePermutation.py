"""
Chapter 01 | Problem 04 - Palindrome Permutation

Problem Statement:
  Given a string, write a function to check if it is a permutation of a palindrome.
  A palindrome is a word or phrase that is the same forwards and backwards.A permutation is 
  a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

Examples:
  "Tact Coa" => True (permutations: "taco cat". "atco cta". etc.)
"""
import unittest

def palindrome_permutation(s):
  char_counter = [0] * 128

  counter = 0
  for c in s:
    if c == ' ':
      continue
    elif char_counter[ord(c)] % 2 == 0:
      counter += 1
    else:
      counter -= 1
    char_counter[ord(c)] += 1
  return counter <= 1


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ("taco cat", True),
    ("atco cat", True),
    (" rac  ecar rara ", True),
    ("chirpingmemaid", False),
    ("aabbc", True),
    ("aaaabbbbcc", True),
    ("aabc", False),
    ("", True)
  ]

  def test_palindrome_permutation(self):
    for [test_s, expected] in self.data:
      actual = palindrome_permutation(test_s)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
