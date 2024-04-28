from sys import stdin

def solve(nums, k):
    n = len(nums)
    dp = [[0 for _ in range(k+1)] for _ in range(n)]

    for i in range(len(nums)):
        for j in range(min(i+1, k)+1):
            if j == 0:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[i-1][j-1] + nums[i], dp[i-1][j])

    max_sum = 0
    for j in range(k+1):
        max_sum = max(max_sum, dp[-1][j])
    return max_sum

def main():
    num_lines = int(stdin.readline())
    for _ in range(num_lines):
        line = stdin.readline().strip()
        if line:
            nums, k = map(int, line.split())
            print(solve(list(map(int, stdin.readline().split())), k))

if __name__ == "__main__":
    main()
