def prob(n):
    # Total number of possible assignments
    tot_assignments = 2 ** n

    # Number of valid assignments
    valid_assignments = 1  # Initialize to 1, as we need to count only valid assignments
    for i in range(1, n + 1):
        valid_assignments *= (n - i + 1)  # For each tower, we have n-i+1 choices

    # Calculate the probability and take modulo
    prob = (valid_assignments * pow(2, n - 1, 998244353)) % 998244353

    return prob
