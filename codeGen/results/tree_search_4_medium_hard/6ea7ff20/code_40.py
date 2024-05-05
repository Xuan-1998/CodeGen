import sys

n = int(input())
p = list(map(int, input().split()))
dp = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if (p[2*i] < p[2*j-1] and not any(k in str(p[2*x]) for x in range(2*i, 2*j)) or
           (p[2*i] > p[2*j-1] and not any(str(k) in str(p[2*x:]) for k in str(p[2*i:2*j]))):
            dp[i][j] = True

for i in range(n):
    for j in range(i+1, n):
        if dp[i][j]:
            print("YES")
            sys.exit(0)

print("NO")
