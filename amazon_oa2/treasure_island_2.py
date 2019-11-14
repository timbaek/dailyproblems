'''
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure.
So you must figure out a shortest route to one of the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from one of the starting point(marked as 'S') of the map and can move one block up, down, left or right at a time.
The treasure island is marked as ‘X’ in a block of the matrix.
Any block with dangerous rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave the map area.
Other areas ‘O’ are safe to sail in.
Output the minimum number of steps to get to any of the treasure.

e.g.
Input
[
[‘S’, ‘O’, ‘O’, 'S', ‘S’],
[‘D’, ‘O’, ‘D’, ‘O’, ‘D’],
[‘O’, ‘O’, ‘O’, ‘O’, ‘X’],
[‘X’, ‘D’, ‘D’, ‘O’, ‘O’],
[‘X', ‘D’, ‘D’, ‘D’, ‘O’],
]

Output
5
'''
import sys
from collections import deque

def bfs(m, q, row, col):
  visited = [[-1 for _ in range(col)] for _ in range(row)]
  while q:
    (x,y), step = q.popleft()

    visited[x][y] = step
    if m[x][y] == "X":
      return step

    for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
      if 0 <= x + dx < row and 0 <= y + dy < col:
        if m[x+dx][y+dy] != 'D' and visited[x+dx][y+dy] == -1:
          q.append(((x+dx, y+dy), step+1))

  return -1

def solution(m):
  if len(m) == 0 or len(m[0]) == 0:
    return -1

  # matrix = [row[:] for row in m]
  row, col = len(m), len(m[0])

  min_dist = sys.maxsize
  for i in range(len(m)):
    for j in range(len(m[0])):
      if m[i][j] == "S":
        q = deque([((i,j),0)])
        min_dist = min(bfs(m,q,row,col), min_dist)

  return min_dist

print(solution([
['S', 'O', 'O', 'S', 'S'],
['D', 'O', 'D', 'O', 'D'],
['O', 'O', 'O', 'O', 'X'],
['X', 'D', 'D', 'O', 'O'],
['X', 'D', 'D', 'D', 'O'],
]))
