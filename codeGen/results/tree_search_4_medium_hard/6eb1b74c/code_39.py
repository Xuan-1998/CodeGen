from collections import defaultdict

def solve():
    n = int(input())
    dp = [[-1] * (n + 1) for _ in range(101)]
    memoization = [-1] * (n + 1)
    dp[0][0] = 0
    for i in range(1, n + 1):
        s_i = input()
        for j in range(i, -1, -1):
            if dp[j][i-1] != -1:
                for k in range(len(s_i)):
                    if t[j+k:i].find(s_i[k:]) != -1:
                        dp[j][i] = min(dp[j][i], dp[j][i-1] + 1)
                        break
        memoization[i] = dp[0][i]
    res = []
    j, i = n, n
    while i > 0:
        for k in range(len(s_i)):
            if t[i-k-1:i].find(s_i[k:]) != -1:
                res.append((k+1, i))
                i -= len(s_i)
                break
    print(memoization[n])
    for pair in res:
        print(pair[0], pair[1])

t = input()
solve()
