import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[False] * (k + 1) for _ in range(n + 1)]

    # initialization
    for i in range(k + 1):
        dp[0][i] = False

    # transition function
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if s[i - 1] <= s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = True

    # base case
    dp[n][k] = dp[n - 1][k]

    # backtrack to find the actual smallest string
    result = []
    i, j = n, k
    while j > 0:
        if s[i - 1] <= s[j - 1]:
            i -= 1
        else:
            result.append(s[j - 1])
            j -= 1

    # print the result in reverse order
    print(''.join(reversed(result)))

if __name__ == '__main__':
    solve()
