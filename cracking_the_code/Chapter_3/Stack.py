from random import randint

class Stack:
  def __init__(self):
    self.stack = []
    self.size = 0
    self.top = None

  def __str__(self):
    vals = [str(x) for x in self.stack]
    return ' -> '.join(vals)

  def push(self, item):
    self.stack.append(item)
    self.top = item

  def pop(self):
    if not self.top: raise Exception

    item = self.stack.pop()
    self.top = self.stack[-1] if self.stack else None

    return item
  
  def peek(self):
    if not self.top: raise Exception
    return self.top

  def is_empty(self):
    return self.top is None

  def generate(self, n, min_val, max_val):
    for i in range(n):
      self.push(randint(min_val, max_val))
    return self
