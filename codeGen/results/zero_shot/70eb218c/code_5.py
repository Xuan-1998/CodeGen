import sys

n, x = map(int, input().split())

# Convert x to a string
x_str = str(x)

while len(x_str) < n:
    x_str = str(int(x_str) * (10 ** len(x_str))) if len(x_str) > 0 else '1'
else:
    if len(x_str) > n:
        print(-1, file=sys.stdout)
    else:
        print(len(x_str) - n, file=sys.stdout)
