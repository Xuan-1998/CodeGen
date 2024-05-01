def solve():
    a, b = map(int, input().split())
    dp = [0] * 315160  # Initialize DP array with zeros
    dp[0] = a ^ b  # Base case

    for i in range(1, 315160):
        dp[i] = (dp[i-1] ^ ((b >> i%31) & 1)) % (10**9 + 7)

    print(sum(dp[:314159]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
