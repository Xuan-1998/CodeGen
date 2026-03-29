n = int(input())
m = int(input())
a = input().strip()
b = input().strip()

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 or j == 1:
            dp[i][j] = min(i, j)
        else:
            max_similarity = 0
            for k in range(min(i, j)+1):
                similarity = dp[i-k-1][j-k-1] + k*4 - i - j
                if similarity > max_similarity:
                    max_similarity = similarity
            dp[i][j] = max_similarity

max_similarity = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 or j == 1:
            continue
        if dp[i][j] > max_similarity:
            max_similarity = dp[i][j]

print(max_similarity)
