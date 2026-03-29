import sys

n, x = map(int, input().split())
count = 0

while len(str(x)) < n:
    count += 1
    if '0' in str(x):
        x *= int('9' * (len(str(x)) - 1))
    else:
        x *= 10

if len(str(x)) == n:
    print(count)
else:
    print(-1)
