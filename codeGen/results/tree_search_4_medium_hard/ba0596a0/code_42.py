def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n):
        for j in range(max(0, i - k), min(i, k) + 1):
            if dp[j]:
                dp[i] = True
                break

    return dp[-1]

k = int(input())  # read the value of k from stdin
stones = list(map(int, input().split()))  # read the list of stone positions from stdin
print(can_cross_stones(stones))  # print the result to stdout
