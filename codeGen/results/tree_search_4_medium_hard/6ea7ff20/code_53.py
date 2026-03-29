===BEGIN CODE===
from collections import defaultdict

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    memo = defaultdict(bool)
    
    for i in range(0, 2*n, 2):
        if p[i] > p[i+1]:
            left, right = p[:i], p[i+1:]
        elif p[i] < p[i+1]:
            left, right = p[:i+1], p[i+2:]
        else:
            left, right = p[:i], p[i:]
        
        if len(left) == 0 or len(right) == 0:
            continue
        
        memo[(left, right)] = True
    
    for i in range(0, 2*n, 2):
        left, right = p[:i], p[i+1:]
        if (left, right) not in memo:
            return "NO"
    
    return "YES"

print(solve())
