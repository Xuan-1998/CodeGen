import sys

def network_sequence(b):
    n = len(b)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    # Edge case: an empty sequence can be obtained from an empty sequence
    dp[0][0] = True

    for i in range(1, n + 1):
        prev_val = b[i - 1]
        for j in range(i, 0, -1):
            if prev_val == j:
                # We can process this element with the current segment
                dp[i][j] = dp[i - 1][j - 1] or (dp[j - 1][j - 1] and dp[i - 1][prev_val])
            else:
                # We cannot process this element with the current segment
                dp[i][j] = False

    for i in range(n + 1):
        if dp[n][i]:
            print("YES")
            return
    print("NO")

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    network_sequence(b)
