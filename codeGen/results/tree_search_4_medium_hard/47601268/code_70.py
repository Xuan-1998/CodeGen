from sys import stdin

def solve():
    n = int(stdin.readline())
    dp = {0: 1}
    
    for i in range(1, n + 1):
        if not has_consecutive_ones(i):
            dp[i] = dp.get(i - 1, 0) + 1
        else:
            dp[i] = dp.get(i - 1, 0)
    
    return dp[n]

def has_consecutive_ones(n):
    bin_str = bin(n)[2:]
    consecutive_ones = False
    
    for digit in bin_str:
        if digit == '1':
            if consecutive_ones:
                return True
            else:
                consecutive_ones = True
        else:
            consecutive_ones = False
    
    return False

print(solve())
