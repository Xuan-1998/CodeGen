n = int(input())
sequence = list(map(int, input().split()))
dp = [0] * (105 + 1)
for x in sequence:
    dp[x] += 1
max_points = sum([i * min(i // 2, i - 1) for i in range(1, n + 1)])
print(max_points)
