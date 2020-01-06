"""
Chapter 02 | Problem 06 - Palindrome

Problem Statement:
  Implement a function to check if a linked list is a palindrome
"""
from LinkedList import LinkedList, ListNode
  
def is_palindrome(head):
  slow = fast = head
  # Find middle node
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  # Reverse the second half
  node = None
  while slow:
    nxt = slow.next
    slow.next = node
    node = slow
    slow = nxt
  # Compare first and second half
  while node:
    if node.val != head.val:
      return False
    node = node.next
    head = head.next
  return True


# Tests
numbers = [1,2,3,4,4,3,2,1]

dummyRoot = ListNode(0)
ptr = dummyRoot
for number in numbers:
  ptr.next = ListNode(number)
  ptr = ptr.next

ptr = dummyRoot.next
ret = is_palindrome(ptr)
print(ret)
