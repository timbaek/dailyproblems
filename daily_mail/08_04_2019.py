'''
링크드 리스트(linked list)의 머리 노드(head node)와 정수 N이 주어지면, 끝에서 N번째 노드(node)를 제거하고 머리 노드(head node)를 리턴하시오.

단, 리스트를 한번만 돌면서 풀어야합니다. N은 리스트 길이보다 크지 않습니다.


Given a head node of a singly linked list, remove the Nth last element and return the head node.


예제)
Input: 1->2->3->4->5, N=2
Output: 1->2->3->5


Input: 1->2->3, N=3
Output: 2->3


Input: 1, N=1
Output: null
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


def solution(head,n):
  size = 1
  cur = p = head
  while cur.next:
    size += 1
    cur = cur.next
    if size > n + 1:
      p = p.next
  
  if size == n:
    return head.next
  else:
    p.next = p.next.next
    return head

# Test 1
t1_input = stringToListNode([1,2,3,4,5])
t1_output = "[1, 2, 3, 5]"
assert(t1_output == listNodeToString(solution(t1_input,2)))

# Test 2
t2_input = stringToListNode([1,2,3])
t2_output = "[2, 3]"
assert(t2_output == listNodeToString(solution(t2_input,3)))

# # Test 3
t3_input = stringToListNode([1])
t3_output = "[]"
assert(t3_output == listNodeToString(solution(t3_input,1)))
