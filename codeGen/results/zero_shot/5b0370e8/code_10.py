def count_bitwise_and_xor(arr):
    n, k = len(arr), arr[0].bit_length()
    dp = [[0] * (1 << k) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1 << k):
            if all((arr[i - 1] & x) >= y for x, y in zip([2 ** k - 1 - j], [j])):
                dp[i][j] = (dp[i - 1][j] + 1) % (10**9 + 7)
            else:
                dp[i][j] = dp[i - 1][j]

    return sum(dp[n]) % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_bitwise_and_xor(arr))
