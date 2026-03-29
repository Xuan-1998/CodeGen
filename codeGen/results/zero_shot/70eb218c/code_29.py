import sys

def solve():
    n, x = map(int, input().split())
    
    if len(str(x)) == n:
        return 0
    
    if 10**(n-1) > x:
        return -1
    
    ops = 0
    for i in range(len(str(x)), n):
        ops += (9*(10**i) // 10**(i-1))
    
    return ops

print(solve())
