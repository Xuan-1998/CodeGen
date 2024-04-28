def dp(i, j):
    if i < 1 or j < 1:
        return 0
    if i == j:
        return 1
    count = 0
    for k in range(1, i // j + 1):
        count += dp(k * j, j)
    return (count % mod) if mod else count

mod = 1000000007
n, k = map(int, input().split())
print(dp(n, k))
