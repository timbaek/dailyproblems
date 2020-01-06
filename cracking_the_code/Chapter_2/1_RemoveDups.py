"""
Chapter 02 | Problem 01 - Remove Dups

Problem Statement:
  Write code to remove duplicates from an unsorted linked list.
  FOLLOW UP
  How would you solve this problem if a temporary buffer is not allowed?
"""
from LinkedList import LinkedList, ListNode

##########################
#        Method 1        #
##########################
def remove_dups_with_buffer(ll):
  if not ll.head: return

  current = ll.head
  num_set = set([current.val])
  while current.next:
    if current.next.val in num_set:
      current.next = current.next.next
    else:
      num_set.add(current.next.val)
      current = current.next
  return ll

##########################
#        Method 2        #
##########################
def merge(l1, l2):
  dummy = tail = ListNode(0)

  while l1 and l2:
    if l1.val < l2.val:
      tail.next, l1 = l1, l1.next
    else:
      tail.next, l2 = l2, l2.next
    tail = tail.next

  tail.next = l1 or l2
  return dummy.next

def merge_sort(head):
  if not head or not head.next:
    return head

  temp, slow, fast = None, head, head

  while fast and fast.next:
    temp, slow, fast = slow, slow.next, fast.next.next

  temp.next = None

  return merge(merge_sort(head), merge_sort(slow))

def remove_dups_without_buffer(head):
  'Merge sort on LinkedList and check duplicates on adjacent nodes'
  ll = merge_sort(head)
  
  slow, fast = ll, ll.next

  while fast:
    if slow.val == fast.val:
      slow.next = fast.next
      fast = fast.next
    else:
      slow, fast = slow.next, fast.next
  
  output = ""
  while ll.next:
    output += "{} -> ".format(ll.val)
    ll = ll.next
  output += str(ll.val)

  print(output)



# Tests
# ll = LinkedList()
# ll.generate(5,0,9)
# print(ll)
# remove_dups_with_buffer(ll)
# print(ll)

numbers = [7,4,5,1,0,7,9]

dummyRoot = ListNode(0)
ptr = dummyRoot
for number in numbers:
  ptr.next = ListNode(number)
  ptr = ptr.next

ptr = dummyRoot.next
remove_dups_without_buffer(ptr)
