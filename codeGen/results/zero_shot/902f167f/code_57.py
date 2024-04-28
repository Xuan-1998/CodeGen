n, m = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i % j == 0 and j % i == 0:
            ans += 1
print(ans)
