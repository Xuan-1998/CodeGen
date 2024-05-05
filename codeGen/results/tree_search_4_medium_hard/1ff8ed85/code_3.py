def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [[False] * (sum(b) + 1) for _ in range(n + 1)]
        prev_val = 0
        for i in range(1, n + 1):
            for total in range(prev_val, sum(b) + 1):
                if total - b[i - 1] >= 0 and dp[i - 1][total - b[i - 1]]:
                    dp[i][total] = True
            prev_val += b[i - 1]
        print("YES" if any(dp[-1]) else "NO")
