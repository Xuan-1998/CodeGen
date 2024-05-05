import sys

def main():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    dp = [[0] * (len(max(strings, key=len)) + 1) for _ in range(n + 1)]
    suffixes = [""] * (n + 1)

    for i in range(1, n + 1):
        for j in range(len(suffixes[i - 1]) + 1):
            dp[i][j] = sys.maxsize
            for k in range(min(j, len(strings[i - 1]))):
                if strings[i - 1][k:] <= suffixes[i - 1][:j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][len(suffixes[i - 2])] + costs[i - 1])
                    break
        suffixes[i] = suffixes[i - 1] + strings[i - 1]

    if dp[n][len(max(strings, key=len)) + 1] == sys.maxsize:
        print(-1)
    else:
        print(dp[n][len(max(strings, key=len)) + 1])

if __name__ == "__main__":
    main()
