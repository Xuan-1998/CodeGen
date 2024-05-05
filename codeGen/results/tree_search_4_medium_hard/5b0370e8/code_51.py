def count_and_xor(n, k):
    MOD = 10**9 + 7
    dp = [[[0] * 2 for _ in range(1 << k)] for _ in range(n+1)]
    
    for i in range(n, -1, -1):
        for mask in range(1 << k):
            if mask == 0:
                break
            xored = sum((a & mask) ^ (a & ~(mask-1)) for a in input().split())
            dp[i][mask][xored % 2] += dp[i+1][mask >> (k - 1)][(xored + 1) % 2]
            dp[i][mask][xored % 2] %= MOD
        dp[i][0][0] = 1
    
    return sum(dp[0][mask][xored % 2] for mask in range(1 << k)) % MOD

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_and_xor(n, k))
