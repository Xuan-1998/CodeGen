def find_good_sequences():
    n, k = map(int, input().split())
    mod = 1000000007

    dp = [[0]*(k+1) for _ in range(n+1)]

    # Initialize the base case: there is only one good sequence of length 1 ending at any number
    for i in range(1, n+1):
        dp[i][1] = 1

    # Fill up the DP table based on the state transition function
    for j in range(2, k+1):
        for i in range(j-1, 0, -1):
            if i % j == 0:
                dp[i][j] = (dp[i][j-1] + sum(dp[t][1] for t in range(i) if t % i == 0)) % mod

    # The answer is the count of good sequences ending at any number with length k
    return sum(dp[i][k] for i in range(n+1))

print(find_good_sequences())
