def can_make_zero(n, arr):
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return all(x == 0 for x in arr[i:j+1])

        result = "NO"
        if all(x <= y for x, y in zip(arr[:i], arr[j:])):
            result = dfs(i - 1, j)
        if all(x <= y for x, y in zip(arr[i:], arr[:j])):
            result = dfs(i, j + 1)

        memo[(i, j)] = result
        return result

    return "YES" if dfs(0, n-1) else "NO"


n = int(input())
for _ in range(n):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if can_make_zero(n, arr) else "NO")
