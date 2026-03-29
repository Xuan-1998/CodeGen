n = int(input())
sequence = list(map(int, input().split()))

result = []
for i in range(2, n+1):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > n:
            result.append(-1)
            break
        x += sequence[i-1]
        y += sequence[i-1]
        y = x - y
    else:
        result.append(y)

print('\n'.join(map(str, result)))
