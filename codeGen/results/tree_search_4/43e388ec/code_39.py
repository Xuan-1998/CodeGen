def solve():
    a, b = [int(x) for x in input().split()]
    dp = [0] * (a.bit_length() + 1)
    
    for i in range(a.bit_length()):
        dp[i+1] = (dp[i] + ((a & (1 << i)) ^ (b >> i))) % (10**9+7)

    print(sum(dp) % (10**9+7))
