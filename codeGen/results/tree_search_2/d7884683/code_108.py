def max_partitions(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    
    def dfs(i, total_sum):
        if i >= n:
            return 0
        
        if arr[i] > total_sum - arr[i]:
            return 1 + dfs(i + 1, total_sum - arr[i])
        
        return max(dfs(i + 1, total_sum), dfs(i + 1, total_sum - arr[i]))
    
    return dfs(0, sum(arr))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
