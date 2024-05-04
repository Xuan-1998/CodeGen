block_counts = [0] * (n + 1)
for num in numbers:
    current_digit = num[0]
    current_length = 1
    while True:
        if num[current_length:] == num[:current_length]:
            block_counts[current_length] += 1
            break
        elif num[current_length] != current_digit:
            break
        current_length += 1

print(*block_counts, sep=' ')
