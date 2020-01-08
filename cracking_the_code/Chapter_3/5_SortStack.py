"""
Chapter 03 | Problem 05 - Sort Stack

Problem Statement:
  Write a program to sort a stack such that the smallest items are on the top.
  You can use an additional temporary stack, but you may not copy the elements
  into any other data structure (such as an array). The stack supports the
  following operations: push, pop, peek, and isEmpty.
"""
from Stack import Stack

def sort_stack(s):
  if s.is_empty(): return s
  
  s_temp = Stack()
  while not s.is_empty():
    temp = s.pop()
    while not s_temp.is_empty() and s_temp.peek() < temp:
      s.push(s_temp.pop())
    s_temp.push(temp)
  return s_temp


# Tests
stack = Stack()
for x in range(1,6):
  stack.push(x)
# stack.generate(5,1,10)
print(stack)
sorted_s = sort_stack(stack)
print(sorted_s)
