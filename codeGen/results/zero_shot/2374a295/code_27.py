n, k = map(int, input().split())
ans = 1
for _ in range(k):
    ans = (ans * n) % 1000000007
    n += 1
print(ans)
