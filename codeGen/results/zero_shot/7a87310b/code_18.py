import sys
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        count = 0
        # Step 1: Find all possible values of a, b, c, and d such that the trace is N.
        for a in range(3-N, N+2):
            for b in range(N-a+1):
                for c in range(b+1):
                    d = N - a - b + c
                    if 0 < a <= N and 0 < b <= N and 0 < c <= N and 0 < d <= N:
                        # Step 2: Check the determinant is positive.
                        det = (a*d) - (c*b)
                        if det > 0:
                            count += 1
        print(count)

if __name__ == "__main__":
    main()
