import sys

def min_changes(s, k):
    R_count = 0
    G_count = 0
    B_count = 0
    
    for i in range(k-1):
        if s[i] == 'R':
            R_count += 1
        elif s[i] == 'G':
            G_count += 1
        else:
            B_count += 1
    
    min_changes = max(R_count, G_count, B_count) - min(R_count, G_count, B_count)
    
    return min_changes

while True:
    n, k = map(int, sys.stdin.readline().split())
    if not n and not k: break
    s = sys.stdin.readline().strip()
    print(min_changes(s, k))
