import sys

c, n = map(int, input().split())
sdp = [[0]*(10001) for _ in range(c+1)]
dp = [[[0]*10**9 for _ in range(101)] for _ in range(c+1)]

for _ in range(n):
    x, y, s = map(int, input().split())
    sdp[s][y+1][x+1] += s

q = int(input())
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    for i in range(1, c+1):
        dp[i][y2][x2][t] -= sum(sdp[i][min(y2,y)][min(x2,x)] - sdp[i][max(y1-1,y)][max(x1-1,x)] for y in range(min(y2,y), max(y1,y)+1) for x in range(min(x2,x), max(x1,x)+1))
    print(sum(dp[i][y2][x2][t] for i in range(1, c+1)))
