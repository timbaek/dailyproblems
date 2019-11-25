'''

Given a matrix, return all elements of the matrix in diagonal order.

'''


def solution(matrix):
  N, M = len(matrix), len(matrix[0])
  row_start, col_start = 0,0
  i, j = 0, 0

  result = []
  while row_start < N and col_start < M:
    r, c = row_start, col_start

    while r >= 0 and r < N and c >= 0 and c < M:
      result.append(matrix[r][c])
      r -= 1
      c += 1
    
    if row_start == N - 1:
      col_start +=1
    else:
      row_start += 1

  return result


# Test 1
t1_input = [[ 1,  2,  3,  4],
            [ 6,  7,  8,  9],
            [11, 12, 13, 14],
            [16, 17, 18, 19]]
t1_output = [1, 6, 2, 11, 7, 3, 16, 12, 8, 4, 17, 13, 9, 18, 14, 19]
assert(t1_output == solution(t1_input))
