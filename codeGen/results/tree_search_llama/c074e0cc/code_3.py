def find_numbers(a, b):
    result = []
    for num in range(a, b + 1):
        digit_sum = 0
        has_even_digit = False
        for i, digit in enumerate(str(num)):
            if int(digit) % 2 == 0:
                has_even_digit = True
            digit_sum += int(digit) ** (i + 1)
        if num == digit_sum and not has_even_digit:
            result.append(num)
    return ' '.join(map(str, sorted(result)))
