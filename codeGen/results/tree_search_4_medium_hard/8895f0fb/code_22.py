def expectedCarries(A, B):
    N = max(len(str(A)), len(str(B)))
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(N+1):
            if i == 0 and j == 0:
                continue
            a, b = int((10**i-1)//9), int((10**j-1)//9)
            carry = max(a, b) >= 5
            dp[i][j] = (dp[i-1][j-1] + (carry and 1)) if i > 0 and j > 0 else 0

    return sum(sum(row) for row in dp) / ((10**N)**2)

T = int(input())
for _ in range(T):
    N = int(input())
    print(expectedCarries(*map(int, input().split())))
