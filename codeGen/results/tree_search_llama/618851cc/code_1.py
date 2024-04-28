A = set(map(int, input().split()))
B = set(map(int, input().split()))
sum_set = set(i + j for i in A for j in B)

for a in A:
    for b in B:
        if (a + b) not in sum_set and a in A and b in B:
            print(a, b)
