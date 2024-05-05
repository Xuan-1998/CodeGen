import sys

def main():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(26)]
    prev_chars = [[set() for _ in range(n + 1)] for _ in range(26)]

    for i in reversed(range(n)):
        for j in range(min(i, n), -1, -1):
            dp[0][i][j] = costs[i] * (i + 1)
            prev_chars[0][i] = set(strings[i])

            for k in range(25, -1, -1):
                if strings[i].startswith('a' * k):
                    dp[k][i][j] = min(dp[k][i][j], dp[0][i][j])
                    prev_chars[k][i] = prev_chars[0][i]

    res = 0
    chars = set()
    for i in range(n - 1, -1, -1):
        if strings[i].startswith(''.join(sorted(chars))):
            res += costs[i]
        else:
            break

    print(res if res < sys.maxsize else -1)

if __name__ == "__main__":
    main()
