from sys import stdin, stdout

def solve():
    A = int(stdin.readline())
    B = int(stdin.readline())

    dp = [[float('inf')] * (B+1) for _ in range(A+1)]
    dp[0][j] = j for j in range(B+1)

    for i in range(1, A+1):
        for j in range(B+1):
            if i >= j:
                for x in range(j+1, i+1):
                    if (x ^ (B - j)) == j:
                        dp[i][j] = min(dp[i][j], x)
    stdout.write(str(-1) if any(x > A for x in dp[A]) else str(dp[A][0]) + ' ' + str(B - dp[A][0]))

if __name__ == "__main__":
    solve()
