from collections import defaultdict

def solve():
    n = int(input())
    colors = input()

    # Initialize a dictionary to store the dynamic programming table
    dp = defaultdict(int)

    # Compute the minimum number of recolors needed using top-down approach
    for i in range(n):
        prev_color = 'R' if i == 0 else colors[i-1]
        dp[(i, prev_color)] = sum(1 for c in colors[:i+1] if c != prev_color) if i > 0 else 0

    # Initialize variables to store the minimum number of recolors and the optimal garland
    min_recolors = float('inf')
    optimal_garland = ''

    # Traverse the dynamic programming table to find the minimum number of recolors and the optimal garland
    for i in range(n):
        prev_color = 'R' if i == 0 else colors[i-1]
        dp_values = [dp[(i, c)] + (1 if c != prev_color else 0) for c in ['R', 'G', 'B']]
        min_recolors_i = min(dp_values)
        optimal_garland_i = colors[:i+1] + min([c for c in ['R', 'G', 'B'] if dp[(i, c)] == min_recolors_i])
        
        # Update the minimum number of recolors and the optimal garland
        if min_recolors_i < min_recolors:
            min_recolors = min_recolors_i
            optimal_garland = optimal_garland_i

    print(min_recolors)
    print(optimal_garland)

solve()
