import sys

def count_binary_numbers(n):
    # Initialize the dp array with size n+1
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: only one number (0) that does not contain consecutive ones

    for i in range(1, n + 1):
        # Check if the binary representation of the current number does not contain consecutive ones
        bin_i = bin(i)[2:]  # Convert integer to binary and remove the '0b' prefix
        has_consecutive_ones = False
        for j in range(len(bin_i) - 1):
            if bin_i[j] == '1' and bin_i[j + 1] == '1':
                has_consecutive_ones = True
                break

        # Update the dp array based on the result
        if not has_consecutive_ones:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    return dp[n]

n = int(sys.stdin.readline())
print(count_binary_numbers(n))
