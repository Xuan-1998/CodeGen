n, m = map(int, input().split())
min_squares = float('inf')
for size in range(1, min(n, m) + 1):
    if n % size == 0 and m % size == 0:
        min_squares = min(min_squares, (n // size) * (m // size))
print(min_squares)
