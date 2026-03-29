def solve():
    n, t = map(int, input().split())
    dp = [0] * (n + 1)
    
    # Pre-compute values for the base case (rounding 0 digits)
    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], round_up(i), round_down(i))
    
    return str(max(dp))

def round_up(i):
    return int(str(frac)[:i+1].replace('.', '')) - (int(str(frac)[:i]).sum() % 10)

def round_down(i):
    return int(str(frac)[:i+1].replace('.', '')) - ((int(str(frac)[:i]).sum() // 5) * 2 + (int(str(frac)[:i]).sum() % 5))

frac = float(input())

print(solve())
