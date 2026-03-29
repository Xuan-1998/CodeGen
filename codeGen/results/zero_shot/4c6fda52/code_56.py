code
n, k = map(int, input().split())
s = input()

min_changes = float('inf')

for i in range(len(s)):
    new_s = s[i:] + s[:i]
    
    changes = 0
    
    for j in range(len(new_s) - k + 1):
        if set(new_s[j:j+k]) == {'R', 'G', 'B'}:
            break
    else:
        for c in new_s:
            if c not in {'R', 'G', 'B'}:
                changes += 1
    
    min_changes = min(min_changes, changes)

print(min_changes)
