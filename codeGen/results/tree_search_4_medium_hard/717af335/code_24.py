def findXY():
    A = int(input())
    B = int(input())

    dp = [[False] * (B+1) for _ in range(A+1)]

    for i in range(A+1):
        for j in range(B+1):
            if i > 0 or j > min(A, B):
                continue
            elif min(i, j) == 0:
                dp[i][j] = True
            else:
                dp[i][j] = dp[min(i, j)][max(0, j-min(i, j))]

    for x in range(A+1):
        for y in range(B+1):
            if dp[x][y]:
                print(f"{x} {y}")
                return

    print(-1)

findXY()
