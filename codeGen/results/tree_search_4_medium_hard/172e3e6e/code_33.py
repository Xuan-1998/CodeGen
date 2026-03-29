from math import comb

def count_good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if a[i - 1] % i != 0:
            dp[i] = 0
        else:
            for k in range(i + 1):
                dp[i] += comb(n - 1, k) * (dp[k] if k > 0 else 1)
    
    print(dp[n] % (10**9 + 7))

count_good_subsequences()
