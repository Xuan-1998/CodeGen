import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    win_teams = []
    
    for i in range(1, n + 1):
        for mask in range(1 << i):
            if not (mask & (mask - 1)):  # check if this is a power of 2
                next_mask = mask | ((mask >> 1) << 1)
                next_dp = dp[i - 1][mask ^ (next_mask - mask)]
                for j in range(i):
                    if (mask & (1 << j)):
                        dp[i][next_mask] = max(dp[i][next_mask], next_dp + int(s[j]))
    
    for i in range(1 << n):
        if dp[n][i] == max(dp[n]):
            win_teams.append(i)
    
    print(*sorted(win_teams), sep='\n')

if __name__ == '__main__':
    solve()
