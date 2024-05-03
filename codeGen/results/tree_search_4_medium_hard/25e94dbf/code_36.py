code block:
n = int(input())
commands = input()
dp = [0] * (n + 1)

for i in range(n + 1):
    max_dist = 0
    for j in range(min(i, len(commands))):
        if commands[j] == "F":
            dist = dp[i - 1] + 1
            if dist > max_dist:
                max_dist = dist
    dp[i] = max_dist

print(max(dp))
