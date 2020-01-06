from random import randint

class ListNode:
  
  def __init__(self, val, nextNode=None):
    self.val = val
    self.next = nextNode

  def __str__(self):
    return str(self.val)

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
  
  def __iter__(self):
    current = self.head
    while current:
      yield current
      current = current.next

  def __str__(self):
    vals = [str(x) for x in self]
    return ' -> '.join(vals)

  def __len__(self):
    result = 0
    node = self.head
    while node:
      result += 1
      node = node.next
    return result

  def add(self, value):
    if self.head is None:
      self.tail = self.head = ListNode(value)
    else:
      self.tail.next = ListNode(value)
      self.tail = self.tail.next
    return self.tail

  def add_to_beginning(self, value):
    if self.head is None:
      self.tail = self.head = ListNode(value)
    else:
      self.head = ListNode(value, self.head)
    return self.head

  def generate(self, n, min_val, max_val):
    self.head = None
    for i in range(n):
      self.add(randint(min_val, max_val))
    return self
