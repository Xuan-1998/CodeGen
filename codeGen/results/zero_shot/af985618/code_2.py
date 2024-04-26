MOD = 998244353

def main():
    n = int(input())
    A = [input().split() for _ in range(n)]

    # DP table initialization
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # Build the DP table
    for op, x in A:
        if op == '+':
            x = int(x)
            for cnt in range(n - 1, -1, -1):
                for k in range(n):
                    dp[cnt + 1][k + x] = (dp[cnt + 1][k + x] + dp[cnt][k]) % MOD
        else:
            for cnt in range(n):
                for k in range(n):
                    dp[cnt][k] = (dp[cnt][k] * 2) % MOD
        for k in range(n):
            dp[0][k] = (dp[0][k] * 2) % MOD

    # Calculate the answer
    answer = 0
    for i, (op, x) in enumerate(A):
        if op == '+':
            x = int(x)
            for k in range(x, n + 1):
                answer = (answer + dp[i][k]) % MOD

    print(answer)

if __name__ == "__main__":
    main()
