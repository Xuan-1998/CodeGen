def min_changes(s, k):
    n = len(s)
    min_changes = float('inf')
    for i in range(n - k + 1):
        cycle = s[i:i+k-1]
        changes = sum(1 for c in cycle if c not in 'RGB')
        min_changes = min(min_changes, changes)
    return min_changes
