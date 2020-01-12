"""
Chapter 08 | Problem 03 - Magic Index

Problem Statement:
  A magic index in an array A[e... n-1] is defined to be an index
  such that A[ i] = i. Given a sorted array of distinct integers,
  write a method to find a magic index, if one exists, in array A.
"""

def magic_index(lst):
  if not lst:
    return False

  left, right = 0, len(lst) - 1
  while left <= right:
    mid = left + (right - left) // 2

    if lst[mid] == mid:
      return mid
    elif lst[mid] < mid:
      left = mid + 1
    else:
      right = mid - 1
  return -1

def wrapper(lst,start,end):
  if end < start:
    return -1

  mid_index = start + (end - start) // 2
  mid_val = lst[mid_index]

  if mid_index == mid_val:
    return mid_index

  left_index = min(mid_val, mid_index - 1)
  left = wrapper(lst, start, left_index)
  if left >= 0:
    return left

  right_index = max(mid_val, mid_index + 1)
  right = wrapper(lst, right_index, end)

  return right

def magic_index_follow_up(lst):
  return wrapper(lst,0,len(lst)-1)

# Tests
print(magic_index([-40,-20,-1,1,2,3,5,7,9,12,13]))
print(magic_index_follow_up([-40,-20,2,2,2,3,4,7,9,12,13]))
