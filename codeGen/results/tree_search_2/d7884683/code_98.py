def partition_array(arr):
    n = len(arr)
    memo = {0: 0}
    for i in range(1, n+1):
        dp = float('inf')
        for j in range(i-1, -1, -1):
            if sum(arr[:j]) == sum(arr[j:i]):
                dp = min(dp, memo.get(j, 0) + 1)
        memo[i] = dp
    return memo[n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_array(arr))
