import sys
from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    signs = list(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    pos_count = defaultdict(int)

    for i in range(1, n + 1):
        if signs[i - 1] == '+':
            pos_count[n - i] += 1
        else:
            pos_count[i - 1] -= 1

        dp[i][i] = (pos_count[i - 1] > 0) - (pos_count[i - 1] < 0)
        
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            pos_sum = sum((signs[k] == '+') - (signs[k] == '-') for k in range(i, j))
            
            if pos_sum > 0:
                dp[i][j] = dp[i][i] + pos_count[j - 1]
            elif pos_sum < 0:
                dp[i][j] = dp[j][j] + (pos_count[i - 1] > 0) - (pos_count[i - 1] < 0)
            else:
                if dp[i][i] == 0:
                    dp[i][j] = 0
                elif pos_sum == 0 and i < j:
                    dp[i][j] = min(dp[k][k + length // 2] for k in range(i, j, max(1, (length - 1) // 2)))
    
    for _ in range(q):
        left, right = map(int, input().split())
        print(min(dp[left][right]))

if __name__ == "__main__":
    solve()
