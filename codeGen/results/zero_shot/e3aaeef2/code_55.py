import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = str(n)
    while m > 0:
        new_result = ''
        for digit in result:
            if digit == '9':
                new_result += '0'
            else:
                new_result += str(int(digit) + 1)
        result = new_result
        m -= 1
    print(len(result) % (10**9 + 7))
