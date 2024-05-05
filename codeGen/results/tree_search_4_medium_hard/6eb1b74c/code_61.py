from collections import defaultdict

def process_input():
    t = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]
    return t, n, s

def solve(t, n, s):
    dp = [[-1] * (len(t) + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for j in range(1, len(t) + 1):
        for i in range(1, n + 1):
            tokens_in_this_step = sum(s[:i].count(ss) for ss in s)
            if j <= tokens_in_this_step:
                dp[i][j] = dp[i-1][j-tokens_in_this_step]
            else:
                for k in range(i):
                    if dp[k][j-k] != -1 and dp[k][j-k] + 1 < dp[i][j]:
                        dp[i][j] = dp[k][j-k] + 1
                        break

    if dp[n][len(t)] == -1:
        return -1
    else:
        min_steps, last_pos = dp[n][len(t)], len(t)
        for i in range(n, 0, -1):
            for j in range(last_pos, -1, -1):
                if dp[i-1][j] != -1 and dp[i-1][j] + 1 < min_steps:
                    min_steps = dp[i-1][j] + 1
                    last_pos = j
        return min_steps

def main():
    t, n, s = process_input()
    result = solve(t, n, s)
    print(result)

if __name__ == "__main__":
    main()
