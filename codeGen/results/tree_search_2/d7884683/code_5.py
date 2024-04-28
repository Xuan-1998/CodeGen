def solve(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    def helper(i, total_sum):
        if i < 0:
            return 0
        left_sum = total_sum - sum(arr[i:])
        if i > 0 and dp[i-1] and left_sum == arr[:(i+1)].index(left_sum):
            return dp[i-1] + 1
        return helper(i-1, total_sum)

    return max(helper(i, sum(arr[:i])) for i in range(n))

while True:
    try:
        t = int(input())
        for _ in range(t):
            n = int(input())
            arr = list(map(int, input().split()))
            print(solve(arr))
    except EOFError:
        break
