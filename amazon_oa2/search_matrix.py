def solution(matrix, target):
  if len(matrix) == 0:
    return False
  
  row, col = 0, len(matrix[0]) - 1
  
  while col >= 0 and row < len(matrix):
    if target < matrix[row][col]: col -= 1
    elif target > matrix[row][col]: row += 1
    else: return True
  
  return False
