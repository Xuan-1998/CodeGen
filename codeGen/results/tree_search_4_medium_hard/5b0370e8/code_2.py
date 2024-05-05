import sys

dp = {}
def solve(n, k):
    if (n, k) in dp:
        return dp[(n, k)]

    if n < 0:
        return 0

    total = 0
    for i in range(2**k-1):
        if i & (i - 1) == 0: # if the number is not a power of 2
            continue
        
        temp = solve(n - 1, k - 1)
        total += temp
        dp[(n - 1, k - 1)] = temp

    for i in range(2**k-1):
        if i & (i - 1) != 0: # if the number is a power of 2
            continue
        
        total += solve(n - 1, k)
    
    return (total % (10**9 + 7))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
