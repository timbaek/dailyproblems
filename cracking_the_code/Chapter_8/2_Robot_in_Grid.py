"""
Chapter 08 | Problem 02 - Robot in Grid

Problem Statement:
  Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
  The robot can only move in two directions, right and down, but certain cells are
  "off limits" such that the robot cannot step on them. Design an algorithm to find
  a path for the robot from the top left to the bottom right.
"""

def find_path(g, r, c, path, visited):
  if r < 0 or c < 0 or g[r][c] == 0:
    return False
  
  p = (r,c)
  if p in visited:
    return False

  is_at_origin = (r == 0) and (c == 0)

  left = find_path(g, r, c - 1, path, visited)
  up = find_path(g, r - 1, c, path, visited)

  if is_at_origin or left or up:
    path.append(p)
    return True
  
  visited.add(p)
  return False

def robot_in_grid(g):
  if not g or len(g) == 0:
    return False
  
  path = []

  m,n = len(g), len(g[0])
  visited = set()

  find_path(g, m-1, n-1, path, visited)

  return path


# Tests
grid = [
  [1,1,1,1],
  [0,1,0,1],
  [1,0,1,1],
  [1,1,1,1]
]
print(robot_in_grid(grid))
