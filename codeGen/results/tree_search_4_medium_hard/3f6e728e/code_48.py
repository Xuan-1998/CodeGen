import math

def solve():
    MOD = 10**9 + 7
    
    N, M, C = map(int, input().split())
    upper_hemispheres = list(map(int, input().split()))
    lower_hemispheres = list(map(int, input().split()))

    dp = [0] * (C + 1)
    dp[0] = 1

    for i in range(1, C + 1):
        total_spheres = N + M
        for j in range(i):
            remaining_upper_hemispheres = upper_hemispheres.count(j+1)
            remaining_lower_hemispheres = lower_hemispheres.count(j+1)
            dp[i] += (dp[j] * math.comb(total_spheres - i, C - i)) % MOD
        dp[i] %= MOD

    for i in range(C + 1):
        print(dp[i], end=' ')
    print()

if __name__ == "__main__":
    solve()
