
def solution(l1,l2):
  if not l1:
    return l2
  elif not l2:
      return l1

  if l1.val < l2.val:
      head, l1 = l1, l1.next
  else:
      head, l2 = l2, l2.next
      
  merged_list = head
  while l1 and l2:
      if l1.val < l2.val:
          head.next, l1 = l1, l1.next
      else:
          head.next, l2 = l2, l2.next
      head = head.next

  head.next = l1 if not l2 else l2

  return merged_list
