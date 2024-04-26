from collections import deque

def find_numbers(a, b):
    result = deque()
    for n in range(a, b+1):
        if sum(int(digit) ** (i+1) for i, digit in enumerate(str(n))) == n:
            result.appendleft(n)
    return list(result)

a, b = map(int, input().split())
print(' '.join(map(str, find_numbers(a, b))))
