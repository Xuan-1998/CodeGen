def min_operations():
    T = int(input())
    for _ in range(T):
        n, r_max, l_min = map(int, input().split())
        parent = list(map(int, input().split()))
        values = [list(map(int, input().split())) for _ in range(n)]
        
        dp = [[float('inf')] * (r_max - l_min + 1) for _ in range(n)]
        for i in range(n):
            if i < parent[i]:
                continue
            for j in range(l_min, values[i][1] + 1):
                dp[i][j - l_min] = min(dp[i][j - l_min], 0)
        
        ans = 0
        for i in range(1, n):
            if parent[i] != -1:
                for j in range(l_min, values[parent[i]][1] + 1):
                    dp[i][j - l_min] = min(dp[i][j - l_min], dp[parent[i]][j - l_min])
        return ans

print(min_operations())
