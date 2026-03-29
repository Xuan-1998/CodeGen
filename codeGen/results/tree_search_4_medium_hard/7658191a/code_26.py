def max_score(arr):
    n, k, z = len(arr), k, z
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: initialize the first row of the table
    dp[0][0] = arr[0]

    # Fill up the table using dynamic programming with memoization
    for i in range(1, n):
        for j in range(min(i + 1, k + 1)):
            if j > z or (i - 1 >= 0 and dp[i - 1][j - 1] != float('inf')):
                # Calculate the maximum score by considering both left and right moves
                dp[i][j] = max(dp[i - 1][j - 1] + arr[i], dp[i - 1][j] - arr[i])
            else:
                # If we've reached the maximum number of moves to the left, set the current score as infinite
                dp[i][j] = float('inf')

    return max(dp[-1])

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr))
