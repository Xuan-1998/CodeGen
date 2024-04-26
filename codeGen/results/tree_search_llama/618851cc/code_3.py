import set

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

B_sorted = sorted(list(B_set), reverse=True)

for a in A_set:
    for b in B_sorted:
        if (b - a) not in (A_set | B_set):
            print(f"{a} {b}")
            break
