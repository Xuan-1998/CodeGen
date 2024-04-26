def find_numbers(a, b):
    result = []
    for num in range(a, b + 1):
        digits = [int(x) for x in str(num)]
        if sum(digit ** i for i, digit in enumerate(digits)) == num:
            result.append(num)
    return sorted(result)

a, b = map(int, input().split())
print(' '.join(map(str, find_numbers(a, b))))
