import sys

def max_xor_sum(A, X):
    n = len(A)
    prefix_xors = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xors[i] = prefix_xors[i - 1] ^ A[i - 1]

    max_sum = 0
    for i in range(1, n + 1):
        left_xor = (prefix_xors[i - 1] if i > 1 else 0) ^ X
        right_xor = (A[i - 1] ^ X)
        max_sum = max(max_sum, left_xor + right_xor)

    return max_sum

def main():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        print(max_xor_sum(A, X))

if __name__ == "__main__":
    main()
