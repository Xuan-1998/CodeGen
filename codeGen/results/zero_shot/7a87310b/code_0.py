import sys

def get_positive_invertible_matrices(n):
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = (a**2 + b**2 - n) / 2.0
            d = (a*b - c*n) / n
            if c > 0 and d > 0:
                count += 1
    return count

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(get_positive_invertible_matrices(N))

if __name__ == "__main__":
    main()
