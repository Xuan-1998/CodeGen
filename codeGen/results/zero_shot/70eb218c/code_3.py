import math

n, x = map(int, input().split())

num_digits_x = int(math.log10(x)) + 1

if n > num_digits_x:
    print(-1)
else:
    if n < num_digits_x:
        print(n - 1)
    else:
        print(num_digits_x - n)
