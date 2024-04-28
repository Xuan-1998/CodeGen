n, m = map(int, input().split())
min_squares = float('inf')

for i in range(1, min(n, m) + 1):
    for j in range(i, min(n, m) + 1):
        if n % i == 0 and m % j == 0:
            min_squares = min(min_squares, (n // i) * (m // j))

print(min_squares)
