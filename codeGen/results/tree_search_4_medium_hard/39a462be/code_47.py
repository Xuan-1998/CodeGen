import sys

def read_input():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    return n, m, A, B

def solve(n, m, A, B):
    memo = {}
    max_score = 0

    for i in range(m):
        for j in range(i + 1):
            k = 0
            while k <= min(i - j + 1, n) and A[j:j+k] == B[i:i+k]:
                k += 1
            score = 4 * k - (i + 1)
            if (i, j, k) not in memo:
                memo[(i, j, k)] = score
            else:
                max_score = max(max_score, memo[(i, j, k)])

    return max_score

if __name__ == "__main__":
    n, m, A, B = read_input()
    print(solve(n, m, A, B))
