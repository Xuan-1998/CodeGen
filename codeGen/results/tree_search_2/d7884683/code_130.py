from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    dp = defaultdict(int)
    
    for i in range(n):
        if sum(arr[:i+1]) == sum(arr[i:]):
            dp[i] = dp.get(i-1, 0) + 1
        else:
            dp[i] = dp.get(i-1, 0)
    
    return dp[n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
