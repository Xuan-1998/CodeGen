import sys

def solve(A, B):
    dp = [[sys.maxsize] * (B + 1) for _ in range(A + 1)]

    for i in range(A + 1):
        for j in range(B + 1):
            if i < j:
                X = (i - (A - i)) // 2
                if 2 * X <= i and 2 * X <= A - i and X >= (B - j) // 2 and B % 2 == 0 or X >= (B - j):
                    dp[i][j] = min(dp[i][j], X)

            else:
                for x in range(min(i, j) + 1):
                    if i - x <= A and j - x <= B and (i - x) ^ (j - x) == B - j:
                        dp[i][j] = min(dp[i][j], x)

    return -1 if dp[A][B] == sys.maxsize else dp[A][B]

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(solve(A, B))
