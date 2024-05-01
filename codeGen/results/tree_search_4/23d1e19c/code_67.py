import sys

def solve(n, m, edges, k, fixed_path):
    dp = [[-1] * 2 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == 0:  # special case for vertex s
            dp[i][0] = 0
            continue

        if i not in fixed_path:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
        else:
            prev_idx = fixed_path.index(i)
            prev_vertex = fixed_path[prev_idx - 1]

            if prev_vertex != i:  # not consecutive in the path
                dp[i][0] = min(dp[i][0], dp[prev_vertex][1])
                dp[i][1] = dp[i][0]
            else:
                dp[i][0] = min(dp[i][0], dp[prev_vertex][0])
                dp[i][1] = dp[i][0]

    return (min(dp[k + 1][1]), max(dp[k + 1][1]))

n, m = map(int, input().split())
edges = [(int(u), int(v)) for _ in range(m)]
k = int(input())
fixed_path = list(map(int, input().split()))

min_recomputation, max_recomputation = solve(n, m, edges, k - 1, fixed_path)
print(min_recomputation, max_recomputation)
