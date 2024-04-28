def max_points(n):
    dp = [[0, False] for _ in range(sum(range(1, n+1)) + 1)]

    for i in range(1, n+1):
        a_i = int(input())
        prev_sum = sum(range(1, i))
        for j in range(prev_sum, -1, -1):
            if dp[j][1]:
                dp[j][0] += 1
            else:
                dp[j][0] = 1
            dp[j][1] = (j % a_i == 0)
        for k in range(prev_sum+1, prev_sum+a_i+1):
            dp[k][0] -= 1

    return max(dp[i][0] for i in range(sum(range(1, n+1)) + 1) if not dp[i][1])

if __name__ == "__main__":
    n = int(input())
    print(max_points(n))
