import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))

    # Check if each element in b can be obtained by splitting a segment from a
    for x in b:
        found = False
        for i in range(1, n-1):  # consider all possible splits
            left_sum = sum(b[:i])
            right_sum = sum(b[i:])
            if abs(left_sum - right_sum) == x:  # match found!
                found = True
                break
        if not found:
            print("NO")
            break
    else:
        print("YES")
