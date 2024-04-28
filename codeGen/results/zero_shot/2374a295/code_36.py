k = int(input())
n = int(input())

ans = 1
for _ in range(k - 1):
    ans *= n
    n += 1
print(ans % (10**9 + 7))
