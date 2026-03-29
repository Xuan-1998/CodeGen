def count_digit_ones(n):
    powers_of_two = int(log2(n)) + 1
    no_digit_ones = powers_of_two

    # Subtract the number of integers with at most one digit 1
    no_digit_ones -= n // 9

    return no_digit_ones
