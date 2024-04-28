def find_pair():
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    for a in A:
        if (a + 200) - a not in A and (a + 200) - a not in B:
            return str(a) + " " + str((a + 200) - a)
    
    for b in B:
        if (b + 200) - b not in A and (b + 200) - b not in B:
            return str(b) + " " + str((b + 200) - b)

print(find_pair())
