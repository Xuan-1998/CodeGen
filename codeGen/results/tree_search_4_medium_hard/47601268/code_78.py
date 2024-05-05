import sys

def count_without_consecutive_ones(n):
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        prev_one = -1
        binary_str = bin(i)[2:]
        for j in range(len(binary_str)):
            if binary_str[j] == '1':
                prev_one = j
                break
        if prev_one == -1:  # No consecutive ones
            dp[i] = True
        else:
            dp[i] = dp[prev_one]

    count = sum(1 for x in dp if not x)
    return count

n = int(input())
print(count_without_consecutive_ones(n))
