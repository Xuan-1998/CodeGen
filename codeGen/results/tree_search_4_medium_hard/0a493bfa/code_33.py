def solve(a, b):
    n = len(a)
    m = len(b)

    # Initialize 2D table dp with dimensions (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: If the array only contains one element, return its value as the beauty
    if n == 1:
        return a[0]

    # Base case: If there are no bad prime numbers, return the sum of the array elements as the beauty
    if m == 0:
        return sum(a)

    # Iterate through the array, for each pivot i
    for i in range(n):
        for j in range(i + 1, n):
            k = gcd(a[i], a[j])
            for p in prime_factors(k):
                if p in b:
                    dp[i][j] += dp[i - 1][p - 1]
                else:
                    dp[i][j] += dp[i - 1][p - 1] + a[i]

    # Return the maximum beauty stored in the last cell of the table (n, n)
    return dp[n - 1][m - 1]


def prime_factors(n):
    factors = []
    for p in range(2, int(n ** 0.5) + 1):
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Read input from stdin
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Print the maximum beauty to stdout
print(solve(a, b))
