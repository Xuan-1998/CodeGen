import math

def solve(n):
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        prev_bit = (i >> (math.log2(i) - 1)) & 1
        cur_bit = i % 2
        if prev_bit != cur_bit and not ((prev_bit == 0 and cur_bit == 1) or (prev_bit == 1 and cur_bit == 0)):
            dp[i] = False
        else:
            dp[i] = True

    count = sum(1 for i in range(n + 1) if not dp[i])
    return count

n = int(input())  # Read input from stdin
print(solve(n))  # Print the result to stdout
