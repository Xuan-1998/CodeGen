def find_numbers_without_consecutive_ones(n):
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        if not (i & (i << 1)):  # Check if the most significant bit is 0
            if i < 2:  # Base case: only one number less than 2 can be represented without consecutive ones
                dp[i] = True
            else:
                for j in range(i):
                    if not (j & ((j + 1) ^ i)):  # Check if the rest of the bits represent a number that does not contain consecutive ones
                        dp[i] = True
                        break

    return sum(1 for x in dp if x)

import sys
input_n = int(sys.stdin.readline())
print(find_numbers_without_consecutive_ones(input_n))
