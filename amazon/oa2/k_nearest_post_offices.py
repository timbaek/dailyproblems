'''
Find the k post offices located closest to you, given your location and a list of locations of all post offices available.
Locations are given in 2D coordinates in [X, Y], where X and Y are integers.

Euclidean distance is applied to find the distance between you and a post office.
Assume your location is [m, n] and the location of a post office is [p, q], the Euclidean distance 
  between the office and you is SquareRoot((m - p) * (m - p) + (n - q) * (n - q)).
K is a positive integer much smaller than the given number of post offices.

e.g.
Input
you: [0, 0]
post_offices: [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3

Output
[[-1, 2], [0, 3], [4, 3]]
'''
import math
import heapq

def euclidean_dist(m, n, p, q):
  return math.sqrt((m - p) * (m - p) + (n - q) * (n - q))

def solution(origin, points, k):
  min_heapq = []
  for i, point in enumerate(points):
    dist = euclidean_dist(origin[0], origin[1], point[0], point[1])
    if i < k:
      heapq.heappush(min_heapq, (-dist, point))
    elif -dist > min_heapq[0][0]:
      heapq.heappushpop(min_heapq, (-dist, point))
  
  print(min_heapq)

  return [x[1] for x in min_heapq]


print(solution([0, 0], [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]], 3))
