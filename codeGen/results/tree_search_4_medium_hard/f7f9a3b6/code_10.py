import sys

def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = [[False] * (n + 1) for _ in range(n + 1)]
    memo = {i: False for i in range(n + 1)}

    for i in range(1, n):
        if s[i] == s[i - 1]:
            for j in range(i + 1, n + 1):
                dp[i][j] = True
        else:
            for k in range(i - 1, -1, -1):
                if dp[k][i - 1]:
                    for m in range(k + 1, i + 1):
                        if a[ord(s[m]) - ord('a')] > 0:
                            memo[i] = True
                            break
                    else:
                        continue
                    break
            else:
                continue

        for j in range(i + 1, n + 1):
            dp[i][j] = (dp[i][i - 1] and memo[j])

    total_ways = dp[0][n - 1]
    max_len = max((m - k) for k, m in enumerate(memo) if memo[m]) % (10**9 + 7)
    min_substrs = min(len(list(filter(None, memo))) + 1 for i in range(n)) % (10**9 + 7)

    print(total_ways % (10**9 + 7))
    print(max_len)
    print(min_substrs)

if __name__ == "__main__":
    solve()
