"""
Chapter 02 | Problem 05 - Sum Lists

Problem Statement:
  You have two numbers represented by a linked list, where each node contains a single digit.
  The digits are stored in reverse order, such that the 1's digit is at the head of the list.
  Write a function that adds the two numbers and returns the sum as a linked list.

Example
  Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
  Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.

Example
  Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
  Output: 9 -> 1 -> 2. That is, 912.
"""
from LinkedList import LinkedList, ListNode

def sum_lists_backwards(l1,l2):
  sum_ll = LinkedList()
  l1_head, l2_head = l1.head, l2.head

  carry_over = 0
  while l1_head and l2_head:
    total = (l1_head.val + l2_head.val) + carry_over
    sum_ll.add(total % 10)

    carry_over = total // 10
    l1_head, l2_head = l1_head.next, l2_head.next

  while l1_head:
    total = l1_head.val + carry_over
    sum_ll.add(total % 10)

    carry_over = total // 10
    l1_head = l1_head.next
  while l2_head:
    total = l2_head.val + carry_over
    sum_ll.add(total % 10)

    carry_over = total // 10
    l2_head = l2_head.next

  if carry_over: sum_ll.add(carry_over)
  
  return sum_ll


def sum_lists_forward(l1,l2):
  pass


# Tests
print("---------- Test 1 ----------")
l1 = LinkedList()
l2 = LinkedList()
l1.generate(3,0,9)
l2.generate(3,0,9)
print("L1: {}".format(l1))
print("L2: {}".format(l2))
ret = sum_lists_backwards(l1, l2)
print("Return = {}".format(ret))

print()

print("---------- Test 2 ----------")
l1.generate(3,0,9)
l2.generate(2,0,9)
print("L1: {}".format(l1))
print("L2: {}".format(l2))
ret = sum_lists_backwards(l1, l2)
print("Return = {}".format(ret))

print()

# print("---------- Test 3 ----------")
# l1.generate(3,0,9)
# l2.generate(3,0,9)
# print(l1)
# print(l2)
# ret = sum_lists_forward(l1, l2)
# print(ret)
