import math

n = int(input())  # Read the input integer n from stdin

n_log_10 = math.floor(math.log10(n))  # Find the highest power of 10 that is less than or equal to n
total_ones = 0

for i in range(n_log_10 + 1):
    ones_in_power_of_10 = (10 ** i) // 5  # Count the number of times 1 appears in powers of 10 from i=0 to i=n_log_10
    total_ones += ones_in_power_of_10

# Add the occurrences of 1 in numbers that are not multiples of 10 (i.e., numbers with a single 1)
total_ones += n // 2  # Count the number of times 1 appears in numbers that are not multiples of 10

print(total_ones)  # Print the total count of digit 1 occurrences to stdout
