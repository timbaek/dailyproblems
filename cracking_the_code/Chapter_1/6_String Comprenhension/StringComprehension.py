"""
Chapter 01 | Problem 06 - String Comprehension

Problem Statement:
  Implement a method to perform basic string compression using the counts of repeated characters. 
  For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not 
  become smaller than the original string, your method should return the original string. You can 
  assume the string has only uppercase and lowercase letters (a - z).
"""
import unittest

def string_comprehension(s):
  count = 1

  compressed_str = ''
  for i in range(1,len(s)):
    if s[i] != s[i-1]:
      compressed_str += s[i-1] + str(count)
      count = 0
    count += 1
  compressed_str += s[i] + str(count)

  return compressed_str if len(compressed_str) < len(s) else s


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ("aabcccccaaa", "a2b1c5a3"),
    ("abcdefgh", "abcdefgh"),
    ("abccccdeefgh", "abccccdeefgh")
  ]

  def test_string_comprehension(self):
    for [test_s, expected] in self.data:
      actual = string_comprehension(test_s)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
