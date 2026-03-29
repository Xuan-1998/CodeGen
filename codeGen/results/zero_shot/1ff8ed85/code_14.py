import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    # Step 1: Check if each element in sequence b is less than or equal to the sum of all previous elements in sequence a
    for i in range(1, n):
        if b[i] > sum(b[:i]):
            print("NO")
            break
    else:
        print("YES")
