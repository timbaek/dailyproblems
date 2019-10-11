'''
Given a list of intervals, merge intersecting intervals.

예제)

Input: [(2,4), (1,5), (7,9)]

Output: [(1,5), (7,9)]


Input: [(3,6), (1,3), (2,4)]

Output: [(1,6)]
'''

def solution(intervals):
  if len(intervals) <= 1:
    return intervals

  temp_intervals = sorted(intervals, key=lambda x: x[0])

  merged_stack = [temp_intervals.pop(0)]
  for cur in temp_intervals:
    prev = merged_stack[-1]
    if cur[0] <= prev[1]:
      prev[1] = max(prev[1], cur[1])
    else:
      merged_stack.append(cur)
    
  return merged_stack

print(solution([[2,4],[1,5],[7,9]]))
print(solution([[3,6],[1,3],[2,4]]))
print(solution([[0,1],[0,1]]))
print(solution([[1,3],[2,6],[8,10],[15,18]]))
