import sys
from scipy.stats import hypergeom

def calculate_probability():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    total_players = sum(s)
    min_required_players = 1
    
    if total_players < n:
        return -1.0
    
    probability = 1 - hypergeom.pmf(0, total_players - min_required_players, total_players, m)
    
    return float(probability)

print(calculate_probability())
