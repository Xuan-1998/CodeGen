import sys

def count_matrices(n):
    count = 0
    for i in range(1, n//2+1):
        if (n - i) % (i * 2) == 0:
            j = (n - i) // (i * 2)
            if i <= j and i*j > 0:
                count += 1
    return count

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(count_matrices(n))
