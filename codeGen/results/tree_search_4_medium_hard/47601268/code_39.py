import sys

def find_count(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: The count for 0 is 1

    for i in range(1, n + 1):
        str_bin = bin(i)[2:]  # Convert i to binary and remove leading zeros
        has_consecutive_ones = False
        consecutive_ones_count = 0

        for j in range(len(str_bin) - 1):
            if str_bin[j] == '1' and str_bin[j + 1] == '1':
                has_consecutive_ones = True
                break
            elif str_bin[j] == '1':
                consecutive_ones_count += 1

        if not has_consecutive_ones:
            dp[i] = dp[consecutive_ones_count]
        else:
            dp[i] = max(dp[consecutive_ones_count], dp[i - 1])

    return dp[n]

n = int(input())
print(find_count(n))
