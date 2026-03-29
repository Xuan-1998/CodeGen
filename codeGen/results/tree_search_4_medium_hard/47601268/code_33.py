def count_non_consecutive_ones(n):
    dp = 1  # base case: there is only one number (0) less than or equal to 0 whose binary representation does not contain consecutive ones.
    for i in range(1, n + 1):
        prev_bit = (i - 1) & 1
        if prev_bit == 0:
            dp += 1
        else:
            dp
    return dp

n = int(input())
print(count_non_consecutive_ones(n))
