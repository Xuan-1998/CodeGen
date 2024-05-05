import sys

n, x = map(int, input().split())

if n > len(str(x)):
    print(-1)
else:
    min_ops = 0
    for i in range(len(str(x))):
        if len(str(x)) - i == n:
            break
        max_digit = int(str(x)[:i+1])
        x *= max_digit
        min_ops += 1
    print(min_ops)
