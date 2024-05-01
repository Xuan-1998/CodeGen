def distinct_sum_sets(nums):
    n = len(nums)
    dp = {}
    res = set()

    def dfs(i, s):
        if (i, s) in dp:
            return dp[(i, s)]
        if i == 0:
            return {s}
        result = set()
        for j in range(1, i+1):
            result.update(dfs(j-1, s-j))
        dp[(i, s)] = result
        return result

    for i in range(n):
        for s in range(i+1):
            res.update(dfs(i, s))

    return sorted(list(res))

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(*distinct_sum_sets(nums), sep=" ")
