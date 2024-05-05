import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n+1):
            if i % 2 == 0: # even length
                for j in range(i-1,-1,-1):
                    if b[j] % 2 == 0 and (dp[j] or not dp[i-j-1]):
                        dp[i] = True
                        break
            else: # odd length
                for j in range(i-1, -1, -1):
                    if b[j] % 2 != 0 and (dp[j] or not dp[i-j-1]):
                        dp[i] = True
                        break
        print('YES' if dp[-1] else 'NO')

solve()
