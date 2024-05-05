import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, X = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        A.sort()
        max_sum = 0
        left, right = 0, N - 1
        while left <= right:
            if A[left] + X <= A[right]:
                max_sum += (A[right] - A[left]) * (right - left)
                left += 1
            else:
                max_sum += (A[right] - A[left]) * (right - left) + X
                break
        print(max_sum)

solve()
