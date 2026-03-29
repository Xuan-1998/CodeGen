n = int(input())
x = int(input())

current_length = len(str(x))

if current_length == n:
    print(0)
else:
    diff = n - current_length
    for _ in range(diff - 1):
        x *= 10

    if x >= 10 ** (n - 1):
        print(-1)
    else:
        print(diff)
