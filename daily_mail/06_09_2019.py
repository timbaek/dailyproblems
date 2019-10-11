'''
Reverse all the words in the given string.

예제)

Input: “abc 123 apple”

Output: “cba 321 elppa”
'''

def reverse_str(s):
  return s[::-1]

def solution(s):
  new_s = ""

  i,j = 0, 0
  for j in range(0,len(s)):
    if s[j] == " ":
      new_s = new_s + reverse_str(s[i:j]) + " "
      i = j + 1
  
  new_s = new_s + reverse_str(s[i:j+1])

  return new_s

print(solution("abc 123 apple"))