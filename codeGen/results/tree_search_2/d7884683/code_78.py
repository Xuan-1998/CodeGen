def max_partitions(arr):
    n = len(arr)
    memo = {}

    def dfs(i, right_sum):
        if (i, right_sum) in memo:
            return memo[(i, right_sum)]

        if i == 0 or i == n - 1:
            return 0

        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])

        if left_sum == right_sum:
            return dfs(i - 1, right_sum)

        result = max(dfs(i - 1, right_sum), dfs(i + 1, right_sum)) + 1
        memo[(i, right_sum)] = result
        return result

    return dfs(0, sum(arr))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))
