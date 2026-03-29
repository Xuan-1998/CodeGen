n = int(input())
moods = list(map(int, input().split()))
dp = [0] * (n + 1)
prev_mood = None

for i in range(1, n + 1):
    if moods[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = max(dp[i - 1], 0)

    if dp[i] > n // 2:
        print("NO")
        exit()

prev_mood = moods[-1]

print("YES" if prev_mood else "NO")
