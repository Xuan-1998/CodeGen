import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

# Sort both arrays based on their absolute values
A.sort(key=abs)
B.sort(key=abs)

# Iterate through the sorted lists to find the desired pair
for a in A:
    for b in B:
        if abs(a + b) not in A and abs(a + b) not in B:
            print(f"{a} {b}")
            sys.exit(0)
