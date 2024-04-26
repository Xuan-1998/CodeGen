def calc_sum_digits(n):
    if n < 10:  # Base case: single-digit numbers
        return n

    total = 0
    for i, digit in enumerate(str(n)):
        total += int(digit) ** (i + 1)
    return total


def find_numbers_with_sum_equal_to_number(a, b):
    result = []
    for num in range(a, b + 1):
        if calc_sum_digits(num) == num:
            result.append(num)

    return sorted(result)


a, b = map(int, input().split())
print(' '.join(map(str, find_numbers_with_sum_equal_to_number(a, b))))
