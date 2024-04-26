MOD = 998244353

def main():
    n = int(input().strip())
    elements = [input().strip().split() for _ in range(n)]

    # dp[i] will store the sum of all subsequences of length i
    dp = [0] * (n + 1)
    dp[0] = 1  # There is one subsequence of length 0, the empty subsequence

    # We will store the sum of values for each position where they can contribute
    contributions = [0] * (n + 1)

    for element in elements:
        if element[0] == '+':
            x = int(element[1])
            # Update contributions for all subsequences where x can be included
            for i in range(n - 1, -1, -1):
                contributions[i + 1] = (contributions[i + 1] + x * dp[i]) % MOD
                dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
        else:
            # Update dp for subsequences that could have included an element but now cannot
            for i in range(1, n + 1):
                dp[i] = (dp[i] + dp[i - 1]) % MOD

    # Sum up the contributions
    result = sum(contributions) % MOD
    print(result)

if __name__ == "__main__":
    main()
