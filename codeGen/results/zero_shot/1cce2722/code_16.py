n = int(input())
a = list(map(int, input().split()))
dp = [0] * (max(a) + 1)
for i in a:
    dp[i] += 1
ans = sum((i+1)*dp[i] for i in range(max(a)//2+1))
print(ans)
