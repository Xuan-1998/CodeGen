import sys

def solve():
    n = int(input())
    s = input()

    dp = [[False] * (n+1) for _ in range(n+1)]
    dp[0][0] = True  # base case: 0 recolors, garland is diverse

    for i in range(1, n+1):
        prev_color = s[i-1]
        for j in range(i+1):
            if (j == 0 and prev_color != s[0]) or \
               (j > 0 and prev_color != s[i-1] and dp[i-1][j-1]):
                dp[i][j] = True

    min_rec = n
    for j in range(n+1):
        if dp[n][j]:
            min_rec = j
            break

    recolors = []
    prev_color = s[0]
    for i in range(1, n):
        if prev_color == s[i]:
            recolors.append(i)
        prev_color = s[i]

    print(min_rec)  # output the minimum number of recolors
    print(''.join(['R' if i in recolors else c for i, c in enumerate(s)]))  # output a diverse garland

solve()
