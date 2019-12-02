'''
2차 정수 배열(2D int array)가 주어지면, 소용돌이 모양으로 원소들을 프린트하시오. 예제를 보시오.

Given a 2D integer array, print all elements in a circular spiral shape starting from [0][0]. See example.


예제)

Input:
[[1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]]



Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
'''


def solution(matrix):
  to_print = ""
  M,N = len(matrix), len(matrix[0])
  
  shiftR, shiftD = True, False

  left, right, top, bottom = 0, N, 0, M

  count = 0
  i,j = 0,0
  while count < M * N:
    count += 1
    to_print += str(matrix[i][j]) + " "

    if shiftR and not shiftD: # Moving Right
      if j < right - 1: j += 1
      else:
        shiftD = True
        i += 1
        top += 1
    elif shiftR and shiftD: # Moving Down
      if i < bottom - 1: i += 1
      else:
        shiftR = False
        j -= 1
        right -= 1
    elif not shiftR and shiftD: # Moving Left
      if j > left: j -= 1
      else:
        shiftD = False
        i -= 1
        bottom -= 1
    else: # Moving Up
      if i > top: i -= 1
      else:
        shiftR = True
        j += 1
        left += 1
  return to_print


# Test 1
t1_input = [
  [1, 2, 3],
  [8, 9, 4],
  [7, 6, 5]
]
print(solution(t1_input))

# Test 2
t2_input = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7]
]
print(solution(t2_input))
