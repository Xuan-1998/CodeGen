n, m = map(int, input().split())
min_squares = float('inf')
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        min_squares = min(min_squares, (n // i) * (m // i))
print(min_squares)
