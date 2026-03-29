from collections import defaultdict

def simulate_program(a):
    n = len(a) + 1
    memo = [[-1] * (10**9 + 2) for _ in range(n)]
    
    for i in range(1, n):
        x = y = 0
        while x <= 0 or x > n:
            if a[x] == 0:
                return -1
            y += a[x]
            x -= a[x]
        
        memo[i][y + 1] = max(memo[i][y + 1], y)
    
    return [max(memo[i]) for i in range(2, n+1)]

n = int(input())
a = list(map(int, input().split()))
print(*simulate_program(a))
