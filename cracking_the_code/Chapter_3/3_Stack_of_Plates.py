"""
Chapter 03 | Problem 03 - Stack of Plates

Problem Statement:
  Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
  Therefore, in real life, we would likely start a new stack when the previous stack
  exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
  SetOfStacks should be composed of several stacks and should create a new stack once
  the previous one exceeds capacity. SetOfStacks. push () and SetOfStacks. pop () should
  behave identically to a single stack (that is, pop ( ) should return the same values
  as it would if there were just a single stack).
"""

class SetOfStacks:

  def __init__(self):
    self.stacks = []
    self.stack = []
    self.size = 0
    self.max_size = 3
    self.top = None

  def push(self, item):
    if self.size == self.max_size:
      self.stacks.append(self.stack)
      self.size, self.stack = 0, []
    
    self.stack.append(item)
    self.top = item
    self.size += 1

  def pop(self):
    if not self.top: raise Exception

    item = self.stack.pop()
    if not self.stack:
      self.stack = self.stacks.pop()
    self.top = self.stack[-1]

    return item
  
  def peek(self):
    if not self.top: raise Exception
    return self.top

  def is_empty(self):
    return self.top is None

sos = SetOfStacks()
for x in range(10):
  sos.push(x)
print(sos.stacks)
print(sos.stack)
print(sos.peek())
sos.pop()
print(sos.stacks)
print(sos.stack)
print(sos.peek())
