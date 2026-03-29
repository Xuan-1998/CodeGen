while True:
    n, k = map(int, input().split())
    s = input()
    
    changes = 0
    for c in set(s):
        count = s.count(c)
        if count < k // 3:  # At least k/3 occurrences of each color are needed
            changes += k // 3 - count
    
    print(changes)
