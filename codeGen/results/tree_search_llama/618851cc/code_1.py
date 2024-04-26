from collections import Counter

A = list(map(int, input().split()))
B = list(map(int, input().split()))

count_A = Counter(A)
count_B = Counter(B)

for a in sorted(count_A.keys()):
    for b in B:
        if (a + b) not in count_A and (a + b) not in count_B:
            print(a, b)
