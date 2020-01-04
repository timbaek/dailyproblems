"""
Chapter 01 | Problem 03 - URLify

Problem Statement:
  Write a method to replace all spaces in a string with '%20: You may assume that 
  the string has sufficient space at the end to hold the additional characters, and that 
  you are given the "true" length of the string. (Note: If implementing in Java, please use 
  a character array so that you can perform this operation in place.)

Examples:
  "Mr John Smith    ", 13 => "Mr%20John%20Smith"
"""
import unittest

def urlify(s,n):
  new_s = ""
  
  # Count the number of non-space characters in the string, then subtract 
  # chars from true length n to see how many spaces we are allowed with '%20'
  chars = 0
  for c in s:
    if c != ' ': chars += 1

  # If we see a space and there are still spaces left to append, append '%20'
  # to output string, otherewise copy current character
  spaces = n - chars
  for c in s:
    if c == ' ' and spaces > 0:
      new_s += '%20'
      spaces -= 1
    elif c != ' ':
      new_s += c
  
  while spaces > 0:
    new_s += '%20'
    spaces -= 1

  return new_s


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [
    ("Mr John Smith ", 13, "Mr%20John%20Smith"),
    ("Mr John Smith ", 14, "Mr%20John%20Smith%20"),
    ("   hi", 7, "%20%20%20hi%20%20"),
    ("", 0, ""),
    ("", 2, "%20%20"),
    ("hel lo", 5, "hello")
  ]

  def test_urlify(self):
    for [test_s, test_n, expected] in self.data:
      actual = urlify(test_s, test_n)
      self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()  
