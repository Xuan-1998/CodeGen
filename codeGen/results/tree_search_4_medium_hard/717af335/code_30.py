def find_min_xor(A, B):
    dp = [[float('inf')] * (B + 1) for _ in range(A + 1)]
    for i in range(A + 1):
        for j in range(B + 1):
            if i <= 0 or j <= 0:
                dp[i][j] = float('inf') if i > 0 else 0
            elif i == j and i % 2 == 0:
                dp[i][j] = 0
            else:
                for k in range(i):
                    for l in range(j):
                        if (i - k) ^ (j - l) <= B - j:
                            dp[i][j] = min(dp[i][j], dp[k][l] + 1)
    return -1 if any(all(x > y for x, y in zip(row, row[1:])) for row in dp) else str(min((x for x, y in dp if A == x + y and B == x ^ y), default=(-1,)))

A = int(input())
B = int(input())
print(find_min_xor(A, B))
