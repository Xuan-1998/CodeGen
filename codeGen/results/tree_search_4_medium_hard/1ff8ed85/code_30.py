import sys

def network_sequence(b):
    n = len(b)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n):
        for j in range(i):
            if abs(b[i-1] - b[i-2]) == b[j]-b[j-1]:
                dp[i] = True
                break
        if not dp[i]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(network_sequence(b))
