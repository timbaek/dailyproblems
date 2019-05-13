"""
Fibonacci sequence starts with 0 and 1 where each fibonacci number is a sum of two previous fibonacci numbers. Given an integer N, find the sum of all even fibonacci numbers.

Ex)

Input: N = 12

Output: 10 // 0, 1, 2, 3, 5, 8 -> 2 + 8 = 10.
13 21 34
"""
def solution(n):
    a,b = 0,1
    sum_so_far = 0
    
    while a + b < n:
        _sum = a + b
        if _sum % 2 == 0:
            sum_so_far += _sum
        
        a = b
        b = _sum
    
    return sum_so_far

def main():
    n1 = 12
    n2 = 7
    n3 = 40
    
    print(solution(n1))
    print(solution(n2))
    print(solution(n3))

if __name__ == '__main__':
    main()
