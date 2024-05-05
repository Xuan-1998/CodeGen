def min_operations(n, x):
    # Initialize the dynamic programming table
    dp = [-1] * (n + 1)

    # Base case: if x is already a single-digit number, return 0
    if len(str(x)) == 1:
        return 0

    for i in range(1, n + 1):
        # Consider all possible last digits that can be achieved by multiplying x by 1-9
        for y in range(10):
            # Calculate the minimum number of operations required to make the length of decimal representation of x equal to i - 1
            prev_ops = dp[i - 1] if i > 1 else min_operations(i - 1, x // 10) + (x % 10 != 0)

            # If it's possible to achieve the last digit y by multiplying x by a digit that has a non-zero unit's place, update dp[i]
            if prev_ops >= 0 and str(x * y).count('0') == 1:
                dp[i] = prev_ops + 1
                break

        # If none of the above conditions are met, it's impossible to make the length of decimal representation of x equal to i, so return -1
        if dp[i] < 0:
            return -1

    return dp[n]
