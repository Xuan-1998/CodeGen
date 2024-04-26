A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

for a in A_set:
    for b in B_set:
        if (a + b) not in A_set and (a + b) not in B_set:
            print(a, b)
            break
