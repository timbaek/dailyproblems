"""
Chapter 04 | Problem 02 - Minimal Tree

Problem Statement:
  Given a sorted (increasing order) array with unique integer elements, 
  write an algo- rithm to create a binary search tree with minimal height.
"""
class Node:
  
  def __init__(self, val=None):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self, level=0):
    ret = "\t"*level+repr(self.val)+"\n"
    ret += self.left.__str__(level+1)
    ret += self.right.__str__(level+1)
    return ret

def wrapper(lst):
  return minimal_tree(lst, 0, len(lst) - 1)

def minimal_tree(lst, start, end):
  if start > end:
    return
  mid = (start + end) // 2
  root = Node(lst[mid])
  root.left = minimal_tree(lst, start, mid - 1)
  root.right = minimal_tree(lst, mid + 1, end)
  return root

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(wrapper(testArray))
