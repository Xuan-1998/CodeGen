def solve():
    n = int(input())
    a = [int(x) for x in input().split()]

    # Initialize dp array
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Count good subsequences ending at each position
    for i in range(2, n+1):
        for j in range(i-1, -1, -1):
            if a[j]%j==0:
                dp[i][j] = (dp[i-1][j-i+1] + 1) % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][j]

    # Calculate the total number of good subsequences
    ans = sum(dp[n][i] for i in range(n+1))

    print(ans)

solve()
