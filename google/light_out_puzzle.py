'''

Given a binary 2D grid (each element can either be a 1 or a 0). You have the ability to choose 
any element and flip its value. The only condition is that when you choose to flip any element 
at index (r, c), the 4 neighbors of that element also get flipped. Find the minimum number of flips
that you need to do in order to set all the elements in the matrix equal to 0. If it's not possible, return -1.

'''

def solution(matrix):
  pass


# Test 1
m1 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
assert(0 == solution(m1))
# Test 2
m2 = [[0, 1, 0],
      [1, 1, 1],
      [0, 1, 0]]
assert(1 == solution(m2))
# Test 3
m3 = [[0, 1, 0],
      [1, 1, 0],
      [0, 1, 1]]
assert(4 == solution(m3))
