from collections import defaultdict

def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        memo = defaultdict(int)
        
        def dfs(i, j):
            if (i, j) not in memo:
                total_sum = sum(arr[:i+1])
                left_sum = 0
                count = 0
                for k in range(i-1, -1, -1):
                    left_sum += arr[k]
                    if left_sum == total_sum - left_sum:
                        count = max(count, dfs(k, i-j))
            memo[(i, j)] = count + (left_sum == total_sum // 2)
            return memo[(i, j)]
        
        print(dfs(n-1, n//2))

max_partitions()
