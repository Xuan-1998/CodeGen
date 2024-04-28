n = int(input())
numbers = list(map(int, input().split()))
dp = {0: 1}
s = 0
ans = []
for num in numbers:
    for i in range(s + 1, s + num + 1):
        if i not in dp:
            dp[i] = 0
        dp[i] += 1
    s += num
for i in sorted(dp.keys()):
    ans.append(str(i))
print(' '.join(ans))
