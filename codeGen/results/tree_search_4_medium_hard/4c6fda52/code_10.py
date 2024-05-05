import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (k+1) for _ in range(n+1)]
    queue = [(0, 0)]

    for i in range(1, n+1):
        for c in range(k+1):
            if i < k:
                dp[i][c] = dp[i-1][c]
            else:
                target = s[(i-k):i]
                while queue and queue[0][0] <= i-k:
                    j, q_c = queue.pop(0)
                    if s[j:i].endswith(target):
                        dp[i][c] = min(dp[i][c], dp[j-1][q_c] + (s[j] != target))
                for d in range(c+1):
                    if i < k:
                        break
                    if c > 0 and d > 0:
                        break
                    if s[:i].endswith(target * ((k-c)//d + 1)):
                        dp[i][c] = min(dp[i][c], dp[j-1][q_c] + (s[j] != target) * d)

    return sum(1 for c in range(k+1) if dp[n][c] > 0)


for _ in range(int(input())):
    print(solve())
