def partition_count(arr):
    memo = {}

    def dfs(n):
        if n == 1:
            return 0
        if n in memo:
            return memo[n]
        if n % 2 == 1 and arr[n//2] == sum(arr[:n//2+1]):
            memo[n] = max(1, dfs((n-1)//2) + (n % 2))
        else:
            memo[n] = 0
        return memo[n]

    return dfs(len(arr))

# Read input from stdin and process each test case
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_count(arr))
