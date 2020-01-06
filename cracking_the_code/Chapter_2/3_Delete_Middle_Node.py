"""
Chapter 02 | Problem 03 - Delete Middle Node

Problem Statement:
  Implement an algorithm to delete a node in the middle (i.e., any node but 
  the first and last node, not necessarily the exact middle) of a singly linked list, 
  given only access to that node.

Example
  Input: the node c from the linked list a -> b -> c -> d -> e -> f
  Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""
from LinkedList import LinkedList, ListNode

def delete_middle_node(ll):
  temp, slow, fast = None, ll.head, ll.head

  while fast and fast.next:
    temp = slow
    slow = slow.next
    fast = fast.next.next

  temp.next = slow.next


# Tests
ll = LinkedList()
ll.generate(20,0,100)
print(ll)
delete_middle_node(ll)
print(ll)
