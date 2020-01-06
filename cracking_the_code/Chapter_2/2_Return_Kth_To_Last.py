"""
Chapter 02 | Problem 02 - Return Kth to Last

Problem Statement:
  Implement an algorithm to find the kth to last element of a singly linked list.
"""
from LinkedList import LinkedList, ListNode

def return_kth_to_last(ll,k):
  i = j = 1
  slow, fast = ll.head, ll.head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    i, j = i + 1, j + 2

  target = j - k if not fast else j - k + 1

  while i < target:
    slow = slow.next
    i += 1

  return slow.val


# Tests
ll = LinkedList()
ll.generate(50,0,100)
print(ll)
ret = return_kth_to_last(ll,3)
print(ret)