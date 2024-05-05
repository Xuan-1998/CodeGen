import sys

def solve():
    N = int(input())  # number of elements in the array
    X = int(input())  # value to add to a subsequence (at most once)
    A = list(map(int, input().split()))  # array A
    max_sum = 0  # maximum sum found so far
    prefix_xor = [0] * (N + 1)  # prefix XOR values

    for i in range(1, N):
        prefix_xor[i] = prefix_xor[i-1] ^ A[i]

    for i in range(1, N):
        for j in range(i+1, N+1):
            total_xor = 0
            for k in range(i-1, j):
                total_xor ^= A[k]
            max_sum = max(max_sum, total_xor + X * (j - i))

    print(max_sum)

if __name__ == "__main__":
    solve()
