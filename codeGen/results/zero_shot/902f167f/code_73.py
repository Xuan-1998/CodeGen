n, m = map(int, input().split())
min_squares = float('inf')

for i in range(n + 1):
    for j in range(m + 1):
        if (i * (i + 1) // 2) >= j and (j * (j + 1) // 2) >= i:
            min_squares = min(min_squares, max(i, j))

print(min_squares)
