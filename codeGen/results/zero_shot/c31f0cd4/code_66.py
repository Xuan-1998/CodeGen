n = int(input())
nums = list(map(int, input().split()))
dp = {0: 1}
ans = set()
for num in nums:
    for i in range(dp.get(0, 0), dp.get(0, 100)+num+1):
        if i not in dp:
            dp[i] = dp.get(i-num, 0) + 1
print(' '.join(map(str, sorted(ans))))
