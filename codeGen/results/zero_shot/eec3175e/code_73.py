n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1 << n):
    s = sum([arr[j] for j in range(n) if (i & (1 << j))])
    ans += s % m == 0
print(ans)
