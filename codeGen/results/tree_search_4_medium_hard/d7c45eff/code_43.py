import sys

def solution():
    n, k = map(int, input().split())
    s = input()

    dp = ["" for _ in range(k+1)]
    memo = {}

    def get_dp(i):
        if i not in memo:
            if i == 0:
                memo[i] = ""
            elif i == 1:
                memo[i] = s[:1]
            else:
                delete = get_dp(i-1)
                duplicate = get_dp(i-1) + s[-1]
                memo[i] = min(delete, duplicate)
        return memo[i]

    for i in range(1, k+1):
        dp[i] = get_dp(i)

    print(dp[k])

if __name__ == "__main__":
    solution()
