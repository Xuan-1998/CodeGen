n, m = map(int, input().split())
ans = (n // 2) * (m // 2)
if n % 2 or m % 2:
    ans += min(n, m)
print(ans)
