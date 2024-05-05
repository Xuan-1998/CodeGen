code
while True:
    len_x = len(str(x))
    if len_x >= n:
        break
    ops += 1
    x *= int(str(x)[-1])

if len_x == n:
    print(ops)
else:
    print(-1)
