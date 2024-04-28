n = int(input())
str1 = input()
str2 = input()

dp = [[0] * (n + 1) for _ in range(n + 1)]
count = 0
max_count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if i > 0 and j > 0:
                count = dp[i][j]
                while True:
                    for k in range(count):
                        print(i - k, j - k)
                    max_count += 1
                    if i >= count or j >= count:
                        break
                    i -= 1
                    j -= 1
        else:
            dp[i][j] = 0

print(max_count)
