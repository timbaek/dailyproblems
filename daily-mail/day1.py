from sys import maxint

"""
Given an integer array, find the largest consecutive sum of elements.
Time Complexity: O(n)

Ex}

Input: [-1, 3, -1, 5]

Output: 7 // 3 + (-1) + 5


Input: [-5, -3, -1]

Output: -1 // -1


Input: [2, 4, -2, -3, 8]

Output: 9 // 2 + 4 + (-2) + (-3) + 8
"""
def solution(arr):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for x in arr:
        max_ending_here = max_ending_here + x
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far

def main():
    arr1 = [-1, 3, -1, 5]
    arr2 = [-5, -3, -1]
    arr3 = [2, 4, -2, -3, 8]
    
    print(solution(arr1))
    print(solution(arr2))
    print(solution(arr3))

if __name__ == '__main__':
    main()
