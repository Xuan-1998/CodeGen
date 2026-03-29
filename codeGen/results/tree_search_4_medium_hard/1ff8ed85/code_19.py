def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        seen = set()
        dp = [[False] * (max(b) + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                dp[i][b[0]] = True
            else:
                prev_val = b[i - 1]
                seen.add(prev_val)
                for j in range(max(b) + 1):
                    if (i == 1 and j not in seen) or (j in seen and abs(j - prev_val) > 1):
                        dp[i][j] = True
        print('YES' if any(all(dp[i][j]) for i in range(n, 0, -1)) else 'NO')

solve()
