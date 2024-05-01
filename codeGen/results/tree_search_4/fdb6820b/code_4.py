from collections import defaultdict

dp = defaultdict(int)

def count_ways(N, i):
    if (N, i) in dp:
        return dp[(N, i)]
    
    if N < 0:
        return 0
    
    if i == 0:
        return 1 if N == 0 else 0
    
    ways = 0
    for k in range(i+1):
        ways += count_ways(N-arr[k], k)
    dp[(N, i)] = ways % (10**9 + 7)
    return dp[(N, i)]

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(count_ways(N, m-1))
