def count_digit_ones(n):
    total_count = 0
    for k in range(10):
        # Count the number of integers less than or equal to 10^k that have a 1 in their ones place
        count_k = sum(1 << i for i in range(k))
        total_count += count_k * (10 ** k)
    return total_count

n = int(input())  # Read input integer n
print(count_digit_ones(n))  # Print the result
