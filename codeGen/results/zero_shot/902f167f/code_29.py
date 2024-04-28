n, m = map(int, input().split())
ans = float('inf')
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        ans = min(ans, (n // i) * (m // i))
print(ans)
