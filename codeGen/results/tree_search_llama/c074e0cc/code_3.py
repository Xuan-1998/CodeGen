def find_numbers(a, b):
    def get_digit_sum(n):
        return sum(int(digit) ** (i + 1) for i, digit in enumerate(str(n)))

    result = []
    for num in range(a, b + 1):
        if num == get_digit_sum(num):
            result.append(str(num))

    return ' '.join(result)

a, b = map(int, input().split())
print(find_numbers(a, b))
