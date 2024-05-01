def find_distinct_sums(set):
    n = len(set)
    total_sum = sum(set)
    dp = [False] * (total_sum + 1)
    dp[0] = True

    for num in set:
        for i in range(total_sum, num - 1, -1):
            if dp[i - num]:
                dp[i] = True

    return sorted([i for i in range(total_sum + 1) if dp[i]])

if __name__ == "__main__":
    n = int(input())
    set = list(map(int, input().split()))
    print(" ".join(str(x) for x in find_distinct_sums(set)))
