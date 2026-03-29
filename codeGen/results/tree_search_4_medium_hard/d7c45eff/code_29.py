from collections import deque

n, k = map(int, input().split())
state = input()

dp = [[deque() for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(min(i,k)+1):
        if j < k:
            dp[i][j].appendleft(dp[i-1][j])
            if state[-1] not in dp[i][j]:
                dp[i][j].appendleft(state[-1])
        else:
            dp[i][j].extendleft(dp[i-1][k])

ans = ''.join(sorted(str(x) for x in dp[n][k]))
print(ans)
