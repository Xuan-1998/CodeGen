def max_score(array, k, z):
    n = len(array)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if k > 0:
            # Right move: add the value at the next index to the score
            dp[i] = max(dp[i - 1], array[i] + dp[i - 1])
            # Left move: add the value at the previous index to the score
            if i <= z:
                dp[i] = max(dp[i], array[i - 1] + dp[i - 1])
        else:
            break

    return dp[n]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    array = list(map(int, input().split()))
    print(max_score(array, k, z))
