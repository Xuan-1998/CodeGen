import sys
from collections import defaultdict

def count_digit_one(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] += dp[i // 10] if i // 10 else 0
        dp[i] += min(i, 9) - (min(i, 9) // 10) * (min(i, 9) != 0)
    
    return sum(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(count_digit_one(n))
