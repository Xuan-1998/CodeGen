from functools import lru_cache

@lru_cache(None)
def partition(i, j):
    if i < 0 or j < 0:  # base case
        return 0
    
    if sum(arr[:i]) == sum(arr[i:]):  # condition for partitioning
        return dp[i-1][j-1] + 1
    
    if j > i:  # swap j and i if necessary
        j, i = i, j
    
    # recursive case: try to partition the array
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i:])
    if left_sum == right_sum:
        return dp[i-1][j-1] + 1
    
    # if no partitioning is possible, backtrack
    return max(partition(i-1, j-1), partition(i-1, j))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    print(partition(n, n))
