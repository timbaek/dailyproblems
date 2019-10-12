'''
Given a string, find the longest substring that does not have duplicate characters.

Input: 'aabcbcbc'
Output: 3 // 'abc'

Input: 'aaaaaaaa'
Output: 1 // 'a'

Input: 'abbbcedd'
Output: 4 // 'bced'
'''

def solution(s):
  if len(s) < 2:
    return 1
  subset = set()

  i, longest_substr = 0, 0
  for j in range(0,len(s)):
    if s[j] in subset:
      longest_substr = max(len(s[i:j]), longest_substr)
      i = j
      subset.clear()
    subset.add(s[j])
  
  longest_substr = max(len(s[i:j]), longest_substr)
  return longest_substr  


print(solution("aabcbcbc"))
print(solution("aaaaaaaa"))
print(solution("abbbcedd"))
print(solution("abcdefg"))
