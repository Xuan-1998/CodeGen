n = int(input())
a = list(map(int, input().split()))
dp = [0] * (max(a) + 1)
ans = 0
for x in a:
    dp[x] += 1
while True:
    if max(dp) > 0:
        ans += max(dp)
        for i in range(1, max(a)):
            if dp[i] > 0 and (i-1 not in a or i+1 not in a):
                break
        for j in range(i-2, -1, -1):
            if j in a:
                del a[a.index(j)]
                dp[j] -= 1
        for j in range(i+3, max(a) + 1):
            if j in a:
                del a[a.index(j)]
                dp[j] -= 1
    else:
        break
print(ans)
