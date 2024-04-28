n = int(input())
a = list(map(int, input().split()))
dp = [0] * (max(a) + 1)
for x in a:
    dp[x] += 1
ans = sum(i*(i-1)//2 for i in dp if i>1)
print(ans)
