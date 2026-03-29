def min_changes(s, k):
    n = len(s)
    min_changes = float('inf')
    
    for i in range(n - k + 1):
        substring_s = s[i:i+k]
        substring_inf = 'RGB' * (k // 3) + 'R' * (k % 3)
        
        if substring_s == substring_inf:
            changes = sum(c1 != c2 for c1, c2 in zip(s, substring_inf))
            min_changes = min(min_changes, changes)
    
    return min_changes

while True:
    n, k = map(int, input().split())
    s = input()
    
    if not (n and k):
        break
    
    print(min_changes(s, k))
