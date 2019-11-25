'''

When people send messages on their phones they sometimes modify word spelling by adding extra letters
for emphasis. For example, if you want to emphasize hello you might write it hellloooooooo. Let's call 
the ls and the os word extensions. Regular text contains 2 or fewer of the same character in a row, while 
word extensions have 3 or more of the same character in a row. Given an input string representing one word, 
write a method that returns the start and end indices of all extensions in the word.

Example 1
Input: "whaaaaatttsup"
Output: [[2, 6], [7, 9]]
Explanation: 
"aaaaa" and "ttt" are twitching letters, so output their starting and ending points.

Example 2
Input: "hellloooooooo"
Output: [[2, 4], [5, 12]]
'''

def solution(s):
  left,right,counter = 0,0,0
  prev = ""

  result = []
  for i in range(len(s)):
    if prev != s[i]:
      if counter > 2:
        result.append([left,right])
      prev = s[i]
      counter = 1
      left, right = i, i
    else:
      counter += 1
      right = i
  
  if counter > 2:
    result.append([left,right])

  return result

assert([[2, 6], [7, 9]] == solution("whaaaaatttsup"))
assert([[2, 4], [5, 12]] == solution("hellloooooooo"))

####### Follow up #######
'''

Now we want to spell-check extended words. You are given a dictionary of words. 
Implement method isExtendedDictionaryWord that will return:

true -> if it is a dictionary word.
true -> if you collapse the extensions in the word and it is a dictionary word.
false -> otherwise.

'''

class SpellChecker:
  def __init__(self, dictionary):
    self.dictionary = set(dictionary)

  def _backtrack(self, compressed_words, cword, word, word_extensions, ext_id):
    if ext_id >= len(word_extensions):
      if word_extensions[-1][1] < len(word) - 1:
        left  = word_extensions[-1][1]+1
        right = left + (len(word) - 1 - word_extensions[-1][1])        
        cword += word[left:right]
      compressed_words.append(cword)
      return

    if ext_id == 0 and word_extensions[0][0] > 0:
      right = word_extensions[0][0]
      cword += word[0:right]
    else:
      slen = word_extensions[ext_id][0] - word_extensions[ext_id-1][1]
      if slen > 1:
        left = word_extensions[ext_id-1][1] + 1
        right = left + (slen - 1)
        cword += word[left:right]
    
    for i in range(1,3):
      interim_str = word[word_extensions[ext_id][0]] * i
      self._backtrack(compressed_words, cword + interim_str, word, word_extensions, ext_id+1)
  
  def getWordExtensions(self, s):
    left,right,counter = 0,0,0
    prev = ""

    result = []
    for i in range(len(s)):
      if prev != s[i]:
        if counter > 2:
          result.append([left,right])
        prev = s[i]
        counter = 1
        left, right = i, i
      else:
        counter += 1
        right = i
    
    if counter > 2:
      result.append([left,right])

    return result

  def isExtendedDictionaryWord(self, s):
    if s in self.dictionary:
      return True
    
    word_extensions = self.getWordExtensions(s)
    if len(word_extensions) == 0: return False

    compressed_words = []
    self._backtrack(compressed_words, "", s, word_extensions, 0)

    for cword in compressed_words:
      if cword in self.dictionary: return True

    return False


# Tests
checker = SpellChecker(["hello"])
assert(True == checker.isExtendedDictionaryWord("hello"))
assert(True == checker.isExtendedDictionaryWord("heeello"))
assert(True == checker.isExtendedDictionaryWord("hellloooooooo"))
assert(False == checker.isExtendedDictionaryWord("xyz"))
