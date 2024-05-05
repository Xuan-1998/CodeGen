import sys

def is_piim(a, b, c, d):
    # Check if the matrix has a trace of N
    if a + d != N:
        return False
    
    # Check if the determinant is positive
    det = a*d - b*c
    if det <= 0:
        return False
    
    return True

N = int(sys.stdin.readline())
count = 0

for a in range(1, N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            for d in range(c+1, N):
                if is_piim(a, b, c, d):
                    count += 1

print(count)
