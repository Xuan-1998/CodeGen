import sys

def count_matrices(n):
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(1, n+1):
                for d in range(c, n+1):
                    if (a + d) == n and (a * d - b * c) > 0:
                        count += 1
    return count

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(count_matrices(n))
