from math import factorial

def count_matrices(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # base case: one matrix with trace 0 has a positive determinant

    for i in range(1, n + 1):
        for j in range(i):  # try different values for top-right element
            if (i - j) % 2 == 0 and factorial(i) // factorial(j) // (i - j) % 2 == 1:  # condition for positive determinant
                dp[i] += dp[j]

    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_matrices(n))
