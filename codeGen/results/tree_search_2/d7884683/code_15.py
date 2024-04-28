def max_partitions(arr):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            dp[i] = True
        else:
            for k in range(i):
                if dp[k] and (left_sum - arr[k] + right_sum) == right_sum:
                    dp[i] = True
                    break

    partitions = 0
    i = n - 1
    while i >= 0:
        if dp[i]:
            partitions += 1
            i -= 1
            while i >= 0 and not dp[i]:
                i -= 1
        else:
            i -= 1

    return partitions - 1


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))


if __name__ == "__main__":
    main()
