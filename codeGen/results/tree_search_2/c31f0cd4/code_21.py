def find_distinct_sums(sets):
    n = len(sets)
    max_sum = sum(sets)

    dp = [[set() for _ in range(max_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0].add(0)

    for i in range(1, n + 1):
        for j in range(1, max_sum + 1):
            if sets[i - 1] <= j:
                dp[i][j] = (dp[i][j - sets[i - 1]] | dp[i - 1][j]) if i > 0 else {dp[i - 1][j - sets[i - 1]]}
            else:
                dp[i][j] = dp[i - 1][j]

    return sorted({sum(subset) for subset in dp[n]})


def main():
    n = int(input())
    sets = list(map(int, input().split()))
    print(" ".join(map(str, find_distinct_sums(sets))))


if __name__ == "__main__":
    main()
