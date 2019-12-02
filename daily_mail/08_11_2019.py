'''
0과 1로 만들어진 2D 정수 배열이 있습니다. 0은 장애물이고 1은 도로일때, 두 좌표가 주어지면, 
첫번째 좌표에서 두번째 좌표까지 가장 가까운 거리를 구하시오. 두 좌표는 모두 도로에서 시작되고 좌, 우, 아래, 위로 
움직이며 대각선으로는 움직일 수 없습니다. 만약 갈 수 없다면 -1을 리턴하시오.


Given a 2D array with 0s and 1s, 0 represents an obstacle and 1 represents a road. 
Find the closest distance between two given points. You must only move up down right left. 
You cannot move through an obstacle.


예제)

Input:
  {{1, 0, 0, 1, 1, 0},
   {1, 0, 0, 1, 0, 0},
   {1, 1, 1, 1, 0, 0},
   {1, 0, 0, 0, 0, 1},
   {1, 1, 1, 1, 1, 1}}

  Start: (0, 0)

  Finish: (0, 4)

Output: 8
'''
import math
import sys

def euclidean_dist(x1,y1,x2,y2):
  return math.sqrt( pow(x2-x1,2) + pow(y2-y1,2) )

def solution(matrix, start, finish):
  f_x, f_y = finish[0], finish[1]
  if not matrix[f_x][f_y]: return -1

  next_point = start
  visited = set()
  visited.add(next_point)

  steps = 0
  while next_point != finish:
    x, y = next_point[0], next_point[1]

    neighbours = []
    if x - 1 >= 0 and matrix[x-1][y] and (x-1,y) not in visited:
      neighbours.append((x-1,y))
    if x + 1 < len(matrix) and matrix[x+1][y] and (x+1,y) not in visited:
      neighbours.append((x+1,y))
    if y - 1 >= 0 and matrix[x][y-1] and (x,y-1) not in visited:
      neighbours.append((x,y-1))
    if y + 1 < len(matrix[0]) and matrix[x][y+1] and (x,y+1) not in visited:
      neighbours.append((x,y+1))

    if not neighbours: return -1

    min_dist = sys.maxsize
    for neighbour in neighbours:
      dist = euclidean_dist(neighbour[0], neighbour[1], f_x, f_y)
      if dist < min_dist:
        min_dist = dist
        next_point = (neighbour[0], neighbour[1])
    visited.add(next_point)
    
    steps += 1
  return steps

# Test 1
t1_input = [
  [1, 0, 0, 1, 1, 0],
  [1, 0, 0, 1, 0, 0],
  [1, 1, 1, 1, 0, 0],
  [1, 1, 1, 1, 1, 1]
]
t1_start = (0,0)
t1_finish = (0,4)
assert(8 == solution(t1_input,t1_start,t1_finish))

# Test 2
t2_input = [
  [1, 0, 0, 0, 1, 0],
  [1, 0, 0, 1, 0, 0],
  [1, 1, 1, 1, 0, 0],
  [1, 1, 1, 1, 1, 1]
]
t2_start = (0,0)
t2_finish = (0,4)
assert(-1 == solution(t2_input,t2_start,t2_finish))
