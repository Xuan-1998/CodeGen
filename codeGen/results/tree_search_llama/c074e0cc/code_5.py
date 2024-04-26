def find_numbers(a, b):
    result = []
    for num in range(a, b+1):
        digit_sum_val = 0
        for i, digit in enumerate(str(num)[::-1]):
            digit_sum_val += int(digit) ** (i+1)
        if num == digit_sum_val:
            result.append(num)
    return sorted(result)

a, b = map(int, input().split())
print(" ".join(map(str, find_numbers(a, b))))
