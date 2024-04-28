n, k = map(int, input().split())
ans = 1
for i in range(k):
    ans *= n - i
print(ans % 100000007)
