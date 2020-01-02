
class Node:
  def __init__(self, val, next, random):
    self.val = val
    self.next = next
    self.random = random

def solution(head):
  deep_copy_dict = {}
        
  if not head:
      return None
  
  cur = head
  while cur:
      deep_copy_dict[cur] = Node(cur.val, None, None)
      cur = cur.next
  
  cur = head
  while cur:
      if cur.next:
          deep_copy_dict[cur].next = deep_copy_dict.get(cur.next)
      if cur.random:
          deep_copy_dict[cur].random = deep_copy_dict.get(cur.random)
      cur = cur.next
  
  return deep_copy_dict[head]
