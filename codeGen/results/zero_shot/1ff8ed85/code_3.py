import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    # Check if the sequence can be obtained from another sequence
    for i in range(1, n):
        if abs(b[i-1] - b[i]) > 1:  # If the difference between two consecutive elements is greater than 1
            print("NO")
            break
    else:
        print("YES")
