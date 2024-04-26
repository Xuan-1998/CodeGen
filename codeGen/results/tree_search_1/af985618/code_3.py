MOD = 998244353

def main():
    n = int(input().strip())
    A = [input().strip().split() for _ in range(n)]

    # dp[i][j] will store the sum of all possible multisets considering the first i elements of A
    # and having j elements in the multiset T.
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: one way to have an empty multiset

    for i in range(1, n + 1):
        if A[i - 1][0] == '+':
            x = int(A[i - 1][1])
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j]  # We can choose not to include the current element
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * x) % MOD  # Include the current element
        else:
            for j in range(i):
                dp[i][j] = (dp[i - 1][j] * (j + 1) + dp[i - 1][j + 1] * j) % MOD  # Erase the smallest element or not

    # Calculate the final answer
    answer = 0
    for i in range(1, n + 1):
        if A[i - 1][0] == '+':
            x = int(A[i - 1][1])
            for j in range(i):
                answer = (answer + dp[i - 1][j] * x) % MOD

    print(answer)

if __name__ == "__main__":
    main()
