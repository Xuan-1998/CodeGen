def count_digit_ones(n):
    total_count = 0
    for i in range(10, n+1):
        # Count ones in tens digit
        total_count += int((i - 1) / 10)
        # Count ones in ones digit
        total_count += (i - 1) % 10 >= 1
    return total_count + 5  # Add ones for numbers from 1 to 9
