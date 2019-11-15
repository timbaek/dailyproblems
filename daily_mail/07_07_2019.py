'''
Given two strings of equal length, check if two strings can be encrypted 1 to 1.

예제)

Input: “EGG”, “FOO”
Output: True // E->F, G->O

Input: “ABBCD”, “APPLE”
Output: True // A->A, B->P, C->L, D->E

Input: “AAB”, “FOO”
Output: False
'''

def solution(s1, s2):
  convert_table = {}

  for i in range(len(s1)):
    if s1[i] not in convert_table:
      convert_table[s1[i]] = s2[i]
  
  convert_str = ""
  for c in s1:
    convert_str += convert_table.get(c)

  return convert_str == s2


# Test 1
assert(True == solution("EGG", "FOO"))
# Test 2
assert(True == solution("ABBCD", "APPLE"))
# Test 3
assert(False == solution("AAB", "FOO"))
