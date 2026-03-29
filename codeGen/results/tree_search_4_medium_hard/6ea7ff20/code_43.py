code
n = int(input())
p = list(map(int, input().split()))
dp = [[False for _ in range(2*2000+1)] for _ in range(2*2000+1)]

for i in range(n):
    for j in range(i+1, 2*n):
        if p[i] > p[j]:
            dp[i][j] = (i==0 and not any(p[k] < p[i] for k in range(j))) or dp[0][j-1]
        else:
            dp[i][j] = (i==0 and not any(p[k] <= p[i] for k in range(j))) or dp[0][j-1]

for i in range(2*n):
    if not dp[n-1][i]:
        print("NO")
        break
else:
    print("YES")
