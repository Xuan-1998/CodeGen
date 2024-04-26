def find_numbers(a, b):
    def digit_sum(n):
        return sum(int(digit) ** i for i, digit in enumerate(str(n)))

    result = []
    for n in range(a, b + 1):
        if all(int(digit) ** i <= 1 for i, digit in enumerate(str(n))):
            if n == digit_sum(n):
                result.append(n)
    return sorted(result)

a, b = map(int, input().split())
print(' '.join(map(str, find_numbers(a, b))))
