'''
두개의 정렬된(sorted) 정수 링크드리스트(linked list)가 주어지면, 두 리스트를 합친 정렬된 링크드리스트를 만드시오.


Given two sorted integer linked lists, merge the two linked lists. Merged linked list must also be sorted.


예제)

Input: 1->2->3, 1->2->3
Output: 1->1->2->2->3->3


Input: 1->3->5->6, 2->4
Output: 1->2->3->4->5->6
'''

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def stringToListNode(numbers):
  # Now convert that list into linked list
  dummyRoot = ListNode(0)
  ptr = dummyRoot
  for number in numbers:
    ptr.next = ListNode(number)
    ptr = ptr.next

  ptr = dummyRoot.next
  return ptr

def listNodeToString(node):
  if not node:
    return "[]"

  result = ""
  while node:
    result += str(node.val) + ", "
    node = node.next
  return "[" + result[:-2] + "]"


def solution(node1, node2):
  if not node1.next:
    return node2
  elif not node2.next:
    return node1

  if node1.val < node2.val:
    head, node1 = node1, node1.next
  else:
    head, node2 = node2, node2.next

  merged_list = head
  while node1 and node2:
    if node1.val < node2.val:
      head.next, node1 = node1, node1.next
    else:
      head.next, node2 = node2, node2.next
    head = head.next

  head.next = node1 if not node2 else node2

  return merged_list


# Test 1
t1_input1 = stringToListNode([1,2,3])
t1_input2 = stringToListNode([1,2,3])
t1_output = "[1, 1, 2, 2, 3, 3]"
assert(t1_output == listNodeToString(solution(t1_input1,t1_input2)))

# Test 2
t2_input1 = stringToListNode([1,3,5,6])
t2_input2 = stringToListNode([2,4])
t2_output = "[1, 2, 3, 4, 5, 6]"
assert(t2_output == listNodeToString(solution(t2_input1,t2_input2)))
