import math

def count_digit_ones(n):
    ones_in_powers_of_ten = int(math.log10(n)) - (math.log10(n) % 1)
    ones_in_odd_numbers = n // 2
    return ones_in_powers_of_ten + ones_in_odd_numbers

n = int(input())
print(count_digit_ones(n))
