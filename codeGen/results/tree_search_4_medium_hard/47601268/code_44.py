import math

def count_binary_no_consecutive_ones(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for bit in range(1, int(math.log2(n)) + 1):
        for i in range(bit, n + 1):
            if (i & (1 << bit)) != 0:
                dp[i] = dp[i ^ (1 << bit)] + dp[max(i - (1 << bit), 0)]
    return dp[n]

if __name__ == "__main__":
    n = int(input())  # Read input from stdin
    print(count_binary_no_consecutive_ones(n))  # Print output to stdout
