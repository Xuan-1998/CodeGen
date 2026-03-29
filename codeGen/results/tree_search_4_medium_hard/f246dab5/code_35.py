import sys

def solve():
    n = int(sys.stdin.readline())
    dp = [[0] * 10**5 for _ in range(10**5)]
    tickets = [20, 50, 120]

    for i in range(n):
        t_i = int(sys.stdin.readline())
        for j in range(min(t_i // 90 + 1, 10**4), -1, -1):
            if dp[j][t_i // 90] + (j * 50) > dp[0][t_i // 90] + tickets[2]:
                break
            dp[j][t_i] = min(dp[j][t_i], dp[j-1][t_i-j*90] + (j * 50))
        for k in range(t_i, -1, -1):
            if dp[t_i-k//60][k%60] + tickets[0] > dp[0][k]:
                break
            dp[t_i][k] = min(dp[t_i][k], dp[t_i-k//60][k%60] + tickets[0])
        for k in range(t_i, -1, -1):
            if dp[k//60][t_i-k%60] + tickets[1] > dp[0][k]:
                break
            dp[k][t_i] = min(dp[k][t_i], dp[k//60][t_i-k%60] + tickets[1])
        print(sum(tickets[i] for i in range(n)) - sum(tickets[i-1] for i in range(1, n)))

if __name__ == "__main__":
    solve()
