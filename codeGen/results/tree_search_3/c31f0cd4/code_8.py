import sys

def get_distinct_sums(nums):
    n = len(nums)
    max_sum = sum(nums)
    dp = [[[] for _ in range(max_sum + 1)] for _ in range(n + 1)]

    def dfs(i, j):
        if i > n or j < 0:
            return []
        if j == 0:
            return [[]]
        if dp[i][j]:
            return dp[i][j]

        result = []
        if nums[i - 1] <= j:
            for subset in dfs(i - 1, j - nums[i - 1]):
                result.append([nums[i - 1]] + subset)
            for subset in dfs(i - 1, j):
                result.append(subset)

        dp[i][j] = result
        return result

    distinct_sums = set()
    for i in range(1, n + 1):
        for j in range(max_sum + 1):
            if dp[i][j]:
                for subset in dp[i][j]:
                    distinct_sums.add(sum(subset))

    print(*sorted(distinct_sums), sep=' ')

# Example usage:
if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    get_distinct_sums(nums)
