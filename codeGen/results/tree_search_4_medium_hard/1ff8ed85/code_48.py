import sys

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    dp = {0: True}
    for i in range(n):
        if i % 2 == 1:
            dp[i+1] = all((dp[j] and ((i-j)%2===(b[i]-b[j])%2)) or ((i-j)%2!==(b[i]-b[j])%2) for j in range(i))
    print("YES" if dp[n] else "NO")
