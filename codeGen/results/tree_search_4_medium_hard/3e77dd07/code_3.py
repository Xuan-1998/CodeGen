import itertools

def is_scrambled(s1, s2):
    n = len(s1)
    m = len(s2)

    # Base case: if either string is empty, return True
    for i in range(n + 1):
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        if i == 0:
            for j in range(m + 1):
                dp[0][j] = True

        # Fill up the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Check all possible permutations of the remaining characters
                    for p in itertools.permutations(s1[:i]):
                        if ''.join(p) == s2[:j]:
                            dp[i][j] = True

        # Return the answer
        return dp[n][m]

# Test the function
s1 = input()
s2 = input()

print(is_scrambled(s1, s2))
