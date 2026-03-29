import sys

def get_positive_invertible_matrices(n):
    count = 0
    for i in range(-n//2 + 1, n//2 + 1):
        for j in range(i+1, n//2 + 1):
            a = i + j - n
            b = i * (i-j) // 2
            if (a**2 + 4*b) **0.5 % 2 == 1:
                count += 1
    return count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(get_positive_invertible_matrices(N))
