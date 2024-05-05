dp = [[0] * (m + 1) for _ in range(n + 1)]
for t in range(1, n + 1):
    for s in range(m + 1):
        if t == 1:  # base case: single vertex
            dp[t][s] = s
        else:
            max_beauty = 0
            for i in range(n - 1, t - 1, -1):
                j = s
                while edges and edges[0][0] == i:  # consider adding an edge from u to v
                    if (edges.pop(0)[0] == t - 1 or edges.pop(0)[1] == t - 1) and not in_tail:
                        j += 1
                        break
                max_beauty = max(max_beauty, dp[i][j])
            dp[t][s] = max_beauty * (t + s)
return dp[n][m]
