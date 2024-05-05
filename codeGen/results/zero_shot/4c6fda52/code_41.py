def min_changes_required():
    n, k = map(int, input().split())
    s = input()
    
    # Calculate the minimum number of changes required
    min_changes = 0
    for i in range(k-1):
        if (i % 3 == 0 and s[i] != 'R') or (i % 3 == 1 and s[i] != 'G') or (i % 3 == 2 and s[i] != 'B'):
            min_changes += 1
    for i in range(k, n):
        if (i % 3 == 0 and s[i] != 'R') or (i % 3 == 1 and s[i] != 'G') or (i % 3 == 2 and s[i] != 'B'):
            min_changes += 1
    
    print(min_changes)
