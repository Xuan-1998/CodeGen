import sys

def garland_recolor(n):
    dp = [[float('inf')] * 3 for _ in range(n)]
    prev_color = None
    min_rec = 0
    
    # Initialize first lamp
    for i in range(3):
        dp[0][i] = 1 if i != 0 else 0
    
    for i in range(1, n):
        for c in range(3):
            if prev_color is not None:
                dp[i][c] = min((dp[i-1][color] + (1 if color != c else 0)) 
                               for color in range(3))
            else:
                dp[i][c] = 1
        prev_color = dp[i].index(min(dp[i]))
    
    # Find the minimum recolors needed
    min_rec = sum(dp[-1])
    
    # Reconstruct the diverse garland
    diverse_garland = []
    for i in range(n):
        diverse_garland.append(next(color for color in range(3) if dp[i][color] == min_rec))
        min_rec -= 1
    
    return min_rec, ''.join([{'R': 'B', 'G': 'R', 'B': 'G'}[c] for c in diverse_garland])

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

print(*garland_recolor(n))
