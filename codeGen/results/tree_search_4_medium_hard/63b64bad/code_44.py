def findFinalValue(n, sequence):
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            a_j = sequence[j - 1]
            if j > i or dp[i][j] < 0:
                dp[i][j] = -1
            else:
                dp[i][a_j + j] = min(dp[i][a_j + j], dp[i][j] + a_j)

    for i in range(n, 0, -1):
        if dp[n][i] != -1:
            return i

    return -1


def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(findFinalValue(n, sequence))


if __name__ == "__main__":
    main()
