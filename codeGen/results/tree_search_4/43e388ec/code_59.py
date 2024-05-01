import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    k = 19
    dp = [0] * (k + 1)
    
    for i in range(k + 1):
        if i == 0:
            dp[i] = (a ^ b) % (10**9 + 7)
        else:
            dp[i] = (dp[i-1] ^ ((b >> i) % 31)) % (10**9 + 7)
    
    return sum(dp)

print(solve())
