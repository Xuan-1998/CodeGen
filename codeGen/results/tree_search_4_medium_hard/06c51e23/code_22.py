import sys
from collections import defaultdict

def solve():
    n, t = map(int, input().split())
    dp = defaultdict(lambda: defaultdict(int))
    fraction = float(input())

    for i in range(n):
        integer_part = int(fraction * 10**i)
        if i == 0:
            max_grade = min(100, integer_part + 1)
        else:
            max_grade = min(100, dp[i-1][t-1] + (integer_part // 10**(i-1)) + 1)

        for j in range(t+1):
            if j >= i:
                round_up = integer_part // 10**i
                round_down = round_up - 1
                if j > i:
                    grade_round_up = dp[i-1][j-i] + round_up * 10**(n-i) + 1
                    grade_round_down = dp[i-1][j-i] + round_down * 10**(n-i) + 1
                    max_grade = min(max_grade, grade_round_up if j > i else max(grade_round_down, integer_part))
            dp[i][j] = max_grade

    print(int(dp[n-1][t]))

if __name__ == "__main__":
    solve()
