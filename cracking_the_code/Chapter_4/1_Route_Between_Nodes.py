"""
Chapter 04 | Problem 01 - Route Between Nodes

Problem Statement:
  Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""
import queue
from Graph import createNewGraph

def bfs(g, src, dest):
  if src == dest:
    return True

  q = queue.Queue(len(g.getNodes()))
  src.visited = True
  q.put(src)
  while not q.empty():
    node = q.get()
    for neighbour in node.getAdjacent():
      if not neighbour.visited:
        if neighbour == dest:
          return True
        else:
          q.put(neighbour)
        neighbour.visited = True
  return False


g = createNewGraph()
n = g.getNodes()
start = n[0]
end = n[5]
print("Start at:", start.getVertex(), "End at: ", end.getVertex())
print(bfs(g, start, end))
