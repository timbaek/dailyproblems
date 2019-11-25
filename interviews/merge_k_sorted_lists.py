import sys

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def mergeKLists_1(lists):
  if not lists:
    return None
  min_index = 0

  head = ListNode(0)
  h = head
  while True:
    is_sorted = True
    min_val = sys.maxsize
    for i in range(len(lists)):
      if lists[i]:
        if lists[i].val < min_val:
          min_index = i
          min_val = lists[i].val
        is_sorted = False
    if is_sorted:
      break
    h.next = lists[min_index]
    h = h.next
    lists[min_index] = lists[min_index].next
  h.next = None
  return head.next

from queue import PriorityQueue

def mergeKLists_2(lists):
  head = point = ListNode(0)
  q = PriorityQueue()

  for l in lists:
    if l:
      q.put((l.val, l))

  while not q.empty():
    val, node = q.get()
    point.next = ListNode(val)
    point = point.next
    node = node.next
    if node:
      q.put((node.val, node))
  return head.next
