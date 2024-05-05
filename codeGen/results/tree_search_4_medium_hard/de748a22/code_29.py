import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        signs = list(map(lambda x: 1 if x == "+" else -1, input()))
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        prefix_sum = [0]
        for sign in signs:
            prefix_sum.append(prefix_sum[-1] + sign)
        
        for i in range(q):
            l, r = map(int, input().split())
            ans = dp[l-1][r]
            for j in range(l-1, r):
                if prefix_sum[j+1] - prefix_sum[l-1] == 0:
                    ans = min(ans, dp[l-1][j])
                else:
                    k = l
                    while k <= j and prefix_sum[k+1] - prefix_sum[l-1] != 0:
                        k += 1
                    ans = min(ans, dp[k-1][j] + abs(prefix_sum[j+1] - prefix_sum[k]))
            print(ans)

if __name__ == "__main__":
    solve()
