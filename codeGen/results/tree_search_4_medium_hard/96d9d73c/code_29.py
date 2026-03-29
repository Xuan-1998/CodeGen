def can_partition(A):
    N = len(A)
    K = int(input())
    M = int(input())

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0:
            return False

        if j < K and A[i-1] - A[0] > M or any(A[i:] - x <= M for x in A[:i]):
            return False

        for partition_end in range(i):
            if dfs(partition_end, max(1, (j+1) // (partition_end + 1))):
                return True

        memo[(i, j)] = False
        return memo[(i, j)]

    return dfs(N-1, K)

def main():
    A = list(map(int, input().split()))
    print(can_partition(A))

if __name__ == "__main__":
    main()
