from collections import defaultdict

def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(len(p) + 1)]

    # Base cases
    for i in range(len(p) + 1):
        dp[i][0] = dp[0][i] = True

    # Fill the table from bottom-up
    for i in range(1, len(p) + 1):
        for j in range(1, min(i, n) + 1):
            if p[i - 1] < p[i - 2]:
                dp[i][j] = (dp[i - 1][j - 1] and p[i - 1] > p[i - j - 1]) or dp[i - j][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # Check if the given permutation can be generated
    for i in range(len(p) - 1, -1, -1):
        for k in range(1, len(p)):
            if p[i] < p[k]:
                if dp[i - k][k]:
                    return "YES"
    return "NO"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print(mergeable(p))


if __name__ == "__main__":
    main()
