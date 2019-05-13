import math

def solution(n, arr1, arr2):
    ret = []
    
    for i in range(0,n):
        row = str(bin(arr1[i]|arr2[i]))[2:]
        encrypted = row.replace('1','#').replace('0', ' ')
        ret.append(encrypted)
    return ret

def main():
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    
    print(solution(n,arr1,arr2))

if __name__ == '__main__':
    main()