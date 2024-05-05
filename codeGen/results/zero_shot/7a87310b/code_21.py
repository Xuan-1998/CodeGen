import sys

def read_input():
    T = int(sys.stdin.readline())
    result = []
    for _ in range(T):
        N = int(sys.stdin.readline())
        result.append(count_matrices(N))
    return result

def count_matrices(N):
    count = 0
    for a in range(1, N // 2 + 1):
        for b in range(a, N // 2 + 1):
            if a + b == N:
                det = (a * (N - a) - b * b)
                if det > 0:
                    count += 1
    return count

if __name__ == "__main__":
    result = read_input()
    for r in result:
        print(r)
