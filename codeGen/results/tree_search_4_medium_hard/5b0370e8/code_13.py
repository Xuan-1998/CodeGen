import sys

def solve():
    t = int(input())
    mod = 10**9 + 7

    dp = [[0] * (1 << k) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for max_and in range(2**k):
            if max_and == 0:
                dp[i][max_and] = 1
            else:
                count = 0
                for and_result in range(max_and + 1):
                    if (and_result & max_and) <= and_result:
                        count += dp[i-1][and_result]
                dp[i][max_and] = count % mod

    ans = sum(dp[n])
    print(ans)

if __name__ == '__main__':
    input()
    solve()
