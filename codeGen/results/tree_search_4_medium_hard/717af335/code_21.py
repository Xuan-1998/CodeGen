def findXY(A, B):
    dp = [[False] * (B + 1) for _ in range(A + 1)]

    for i in range(A + 1):
        for j in range(min(i, B) + 1):
            if i - j >= 0 and (j ^ (i - j)) < min(i, B):
                dp[i][j] = True

    for i in range(A, -1, -1):
        for j in range(B, -1, -1):
            if dp[i][j]:
                X = i
                Y = j ^ X
                return f"{X} {Y}"

    return "-1"

A = int(input())
B = int(input())

print(findXY(A, B))
