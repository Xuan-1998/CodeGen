from collections import deque

def min_operations(A):
    N = len(A)
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    queue = deque([(0, 0)])

    while queue:
        i, prev_idx = queue.popleft()
        for j in range(prev_idx):
            if A[j] < A[i]:
                dp[i] = min(dp[i], dp[j] + 1)
        if i < N - 1:
            queue.append((i + 1, i))

    return dp[N - 1]

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(min_operations(A))
