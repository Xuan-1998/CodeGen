from collections import defaultdict

def can_partition(arr, k, m):
    n = len(arr)
    memo = defaultdict(bool)

    def dfs(i, j):
        if memo[(i, j)]:
            return True
        if i >= n or j < 0:
            return False
        if j == 1:
            return all(abs(arr[i] - x) <= m for x in arr[:i])
        if arr[i] > m:
            return False
        memo[(i, j)] = any(dfs(i-1, j-1) and abs(arr[i] - x) <= m for x in arr[:i])
        return memo[(i, j)]

    result = float('inf')
    for i in range(n):
        if dfs(i, k):
            result = min(result, i)
            break
    return result != float('inf')

if __name__ == "__main__":
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(can_partition(arr, k, m))
