import sys

def count_permutations(n):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base case: there is only one way to create an empty collection
    for i in range(n+1):
        dp[i][0] = 1

    # Fill up the dynamic programming table
    for length in range(1, n+1):
        for first_element_index in range(length):
            last_element_index = length - 1
            if M[first_element_index] != M[last_element_index]:
                dp[length][last_element_index] = (dp[length-1][last_element_index-1] + dp[length-1][last_element_index]) % MOD
            else:
                # If all elements are the same, there is only one way to create V
                dp[length][last_element_index] = 1

    return dp[n][n-1]

# Read input from stdin
n = int(input())
M = list(map(int, input().split()))

print(count_permutations(n))
