from collections import defaultdict

def diverse_garland(n, s):
    dp = {(i, c): i if c != 'R' else float('inf') for i in range(n) for c in set(s)}
    
    for i in range(1, n):
        for prev_c in set(s[:i]):
            for new_c in set(s[i:i+1]):
                dp[(i, new_c)] = min(dp[(i-1, prev_c)], dp[(i, new_c)]) + (0 if new_c != prev_c else 1)
    
    min_recolor = float('inf')
    final_garland = ''
    
    for i in range(n):
        for c in set(s[i:]):
            if dp[(n-1, c)] < min_recolor:
                min_recolor = dp[(n-1, c)]
                final_garland = s[:i] + ['R' if c == 'G' else 'G' if c == 'B' else c for _ in range(n-i)]
    
    return str(min_recolor), final_garland

n = int(input())
s = input().strip()

print(*diverse_garland(n, s))
