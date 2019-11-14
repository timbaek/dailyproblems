'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure. 
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
The treasure island is marked as ‘X’ in a block of the matrix. ‘X’ will not be at the top-left corner.
Any block with dangerous rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave the map area.
Other areas ‘O’ are safe to sail in. The top-left corner is always safe.
Output the minimum number of steps to get to the treasure.

e.g.
Input
[
  [‘O’, ‘O’, ‘O’, ‘O’],
  [‘D’, ‘O’, ‘D’, ‘O’],
  [‘O’, ‘O’, ‘O’, ‘O’],
  [‘X’, ‘D’, ‘D’, ‘O’],
]

Output
Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
'''
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

  row, col = len(m), len(m[0])

  q = deque([((0,0),0)])
  
  return bfs(m,q,row,col)

print(solution([
  ['O', 'O', 'O', 'O'],
  ['D', 'O', 'D', 'O'],
  ['O', 'O', 'O', 'O'],
  ['X', 'D', 'D', 'O'],
]))
