from collections import defaultdict

def solve():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    substrings = defaultdict(int)

    # Preprocess the strings and store the substrings
    for i in range(2, N + 1):
        for j in range(2, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[0][i][j] = dp[0][i - 1][j - 1] + 1
                substrings[(str1[:i], str2[:j])] += 1

    # Compute the maximum number of common non-overlapping substrings
    max_length = 0
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            if dp[0][i][j] > max_length:
                max_length = dp[0][i][j]

    print(max_length)

if __name__ == "__main__":
    solve()
