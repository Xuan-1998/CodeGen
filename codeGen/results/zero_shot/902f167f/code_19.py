n, m = map(int, input().split())
ans = 0
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        ans += (n // i) * (m // i)
print(ans)
