def max_partitions(arr):
    n = len(arr)
    dp = {}

    def dfs(i, right_sum):
        if (i, right_sum) in dp:
            return dp[(i, right_sum)]
        if i == 0 or i == n - 1:
            return 1

        left_sum = sum(arr[:i])
        diff_sum = left_sum - right_sum
        max_partitions_here = dfs(i-1, right_sum + arr[i]) + dfs(n-1, diff_sum)
        dp[(i, right_sum)] = max_partitions_here
        return max_partitions_here

    max_partitions_here = 0
    for i in range(1, n-1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            max_partitions_here = dfs(i, 0)
            break
    return max_partitions_here

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))

if __name__ == "__main__":
    main()
