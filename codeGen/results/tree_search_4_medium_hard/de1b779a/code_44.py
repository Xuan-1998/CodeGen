import sys

def calculate_max_profit(n, m, c0, d0, ai, bi, ci, di):
    dp = [[[0 for _ in range(2)] for _ in range(m+1)] for _ in range(dmax+1)]

    # Initialize the base cases
    for i in range(m+1):
        dp[0][i][0] = 0

    for i in range(dmax+1):
        dp[i][0][0] = 0

    for dough_left in range(1, dmax+1):
        for stuffings_used in range(2):  # Whether any stuffing has been used yet
            available_stuffs = list(range(m))
            if not stuffings_used:
                available_stuffs.sort()
            else:
                available_stuffs = [i for i in range(m) if ai[i] > 0]

            max_profit = 0
            for i, stuffing_type in enumerate(available_stuffs):
                if bi[stuffing_type] <= dough_left and ci[stuffing_type] + c0 <= n:
                    # Calculate the maximum profit by using this stuffing type
                    dp_dough_left = min(dough_left - bi[stuffing_type], ci[stuffing_type])
                    dp_max_profit = di[stuffing_type] * (n - dp_dough_left // ci[stuffing_type]) + dp_dough_left % ci[stuffing_type]
                    if dp_dough_left > 0:
                        max_profit = max(max_profit, dp_dough_left, dp_max_profit)
                    else:
                        max_profit = max(max_profit, dp_max_profit)

            # Update the DP array
            for i in range(m+1):
                dp[dough_left][i][stuffings_used] = max(dp[dough_left][i][stuffings_used], max_profit + dp[max(0, dough_left - bi[i])][i-1][not stuffings_used])

    return max(max(dp[n][i][j] for i in range(m+1) for j in (False, True)))

# Read input from stdin
n = int(input())
m = int(input())
c0 = int(input())
d0 = int(input())

ai = [int(input()) for _ in range(m)]
bi = [int(input()) for _ in range(m)]
ci = [int(input()) for _ in range(m)]
di = [int(input()) for _ in range(m)]

print(calculate_max_profit(n, m, c0, d0, ai, bi, ci, di))
