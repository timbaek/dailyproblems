
def backtrack(combinations, letters, s):
  if not letters[1:]:
    for letter in letters[0]:
      combinations.append(s+letter)
    return

  for letter in letters[0]:
    backtrack(combinations, letters[1:], s+letter)

def letterCombinations(digits):
  book = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }

  letters = []
  for num in digits:
    letters.append(book.get(num))
  
  combinations = []
  backtrack(combinations, letters, "")
  
  return combinations

letterCombinations("234")