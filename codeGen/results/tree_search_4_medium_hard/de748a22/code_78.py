from collections import defaultdict

def min_elements_to_remove(signs):
    n = len(signs)
    q = int(input())

    dp = [[False] * (n+1) for _ in range(n+1)]
    memo = defaultdict(int)

    for i in range(1, n+1):
        if signs[i-1] == "+":
            dp[i][i] = True
        else:
            dp[i][i] = False

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            sign_sum = sum(signs[k] for k in range(i, j+1))
            if memo[sign_sum]:
                dp[i][j] = True
            else:
                dp[i][j] = any(dp[i-1][k] or dp[k+1][j] for k in range(i, j))

    for _ in range(q):
        l, r = map(int, input().split())
        ans = min(0 if not dp[l][r] else r-l+1, 1) if sum(signs[k] for k in range(l-1, r)) % 2 == 0 else float('inf')
        print(min(ans, r-l))

min_elements_to_remove(input().strip().split())
