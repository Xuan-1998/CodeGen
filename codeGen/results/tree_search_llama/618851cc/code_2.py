n, = map(int, input().split())
A = list(map(int, input().split()))
m, = map(int, input().split())
B = list(map(int, input().split()))

a_min = min(A)
b_max = max(B)

found = False

for a in A:
    for b in B:
        if a + b not in (i for i in A) and a + b not in (j for j in B):
            print(a, b)
            found = True
            break
    if found: 
        break

if not found:
    # If no pair is found, the problem statement guarantees that at least one pair exists
    # Therefore, we can just take any a from A and any b from B (except for pairs already checked above)
    print(A[0], B[-1])
