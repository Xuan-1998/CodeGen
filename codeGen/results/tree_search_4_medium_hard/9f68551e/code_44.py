// Begin Solution

n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [0] * (max(k) + 1)
last_kill = -1

for i in range(n-1,-1,-1):
    for j in range(last_kill+1,k[i]+1):
        if h[i] > dp[j]:
            dp[j] = max(dp[j],h[i])
        else:
            last_kill = j

min_mana = 0
for i in range(len(dp)-1, -1, -1):
    if i > 0 and dp[i-1] < dp[i]:
        min_mana = i + 1
        break

print(min_mana)
