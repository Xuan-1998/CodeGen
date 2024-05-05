import sys

def is_invertible(a, b, c, d):
    if (a*d - b*c) == 0:
        return False
    else:
        return True

def calculate_trace(a, b, c, d):
    return a + d

def calculate_determinant(a, b, c, d):
    return a*d - b*c

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for a in range(1, N+1):
        for b in range(N-a+1):
            for c in range(b+1):
                for d in range(c+1):
                    if is_invertible(a, b, c, d) and calculate_trace(a, b, c, d) == N:
                        if calculate_determinant(a, b, c, d) > 0:
                            count += 1
    print(count)
