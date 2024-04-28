n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for a in A:
    for b in B:
        if (a + b) not in A and (a + b) not in B:
            print(a, b)
            break
