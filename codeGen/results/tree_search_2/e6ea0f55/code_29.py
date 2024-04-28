from sys import stdin

def solve(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(k + 1):
        dp[0][i] = nums[0]

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            dp[i][j] = max(dp[i-1][max(0, j-k)], nums[i] + dp[max(0, i-k)][min(k, j)])

    return max(max(row) for row in dp)

if __name__ == "__main__":
    input_nums = list(map(int, stdin.readline().strip().split()))
    k = int(stdin.readline())
    print(solve(input_nums, k))
