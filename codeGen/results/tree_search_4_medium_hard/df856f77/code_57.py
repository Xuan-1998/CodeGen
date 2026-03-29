from collections import defaultdict

def min_operations():
    n = int(input())
    arr = list(map(int, input().split()))
    memo = defaultdict(int)
    
    dp = [defaultdict(int) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1, arr[i]+1):
            if not (arr[i] > j): 
                dp[i][j] = dp[i-1].get(arr[i-1], float('inf')) + 1
            else:
                dp[i][j] = memo.get(j, float('inf'))
        memo[arr[i]] = dp[i][arr[i]]
    
    return min(dp[-1].values())

print(min_operations())
