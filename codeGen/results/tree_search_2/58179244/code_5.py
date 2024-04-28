from collections import defaultdict

def garland_diversity():
    n, s = map(int, input().split())
    dp = [[float('inf')] * 3 for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        prev_c = int(s[i - 1])  # previous lamp's color
        for c in range(3):  # current lamp's color (R, G, or B)
            if c == prev_c:  # same color as the previous lamp
                dp[i][c] = min(dp[i][c], dp[i - 1][prev_c] + 1)  # recolor this lamp
            else:
                dp[i][c] = min(dp[i][c], dp[i - 1][prev_c])  # keep the same color

    r, c = min((dp[n][i], i) for i in range(3))
    t = [chr(c + ord('R')) if c == 0 else (chr(c + ord('G')) if c == 1 else 'B')] * n
    print(r)
    print(''.join(t))

garland_diversity()
