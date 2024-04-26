A = set(map(int, input().split()))
B = set(map(int, input().split()))
AB = sorted(list(A.union(B)))

for i in range(len(AB) - 1):
    if AB[i] + AB[i+1] not in A and AB[i] + AB[i+1] not in B:
        print(AB[i], AB[i+1])
        break
