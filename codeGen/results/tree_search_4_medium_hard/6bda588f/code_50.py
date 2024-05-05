def min_value(n, s, memo={}):
    if (n, s) in memo:
        return memo[(n, s)]

    if n == 1:
        return [0][0]

    min_val = float('inf')
    for x in range(s+1):
        y = a[n-1] - x
        val = min_value(n-1, y, memo)[0]
        min_val = min(min_val, x*y + val)

    memo[(n, s)] = min_val
    return [min_val]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_value(n, s)[0])
