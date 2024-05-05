def min_operations(root):
    n = root[0]
    parent = [0] + root[1:]
    range_value = [[int(x) for x in line.split()] for line in input().split('\n')]

    dp = [[float('inf')] * (range_value[n-1][1]+1) for _ in range(n)]
    dp[0][0] = 0

    for i in range(1, n):
        p_i = parent[i]
        r_p_i = range_value[p_i][1]

        for j in range(r_p_i+1):
            if j <= r_i:
                dp[i][j] = min(dp[i][j], dp[p_i][max(0, j-r_p_i)] + 1)
            else:
                dp[i][j] = float('inf')

    return dp[n-1][-1]

T = int(input())
for _ in range(T):
    root = list(map(int, input().split()))
    print(min_operations(root))
