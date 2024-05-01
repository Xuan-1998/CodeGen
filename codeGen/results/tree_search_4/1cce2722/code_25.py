from bisect import bisect_left, bisect_right

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return 1
        if a[i] not in [a[i-1]-1, a[i-1]+1]:
            result = dp(i-1)
        else:
            left = bisect_left(a[:i], a[i-1])
            right = bisect_right(a[:i], a[i-1])
            if left == 0 and right == i:
                result = dp(i-2) + 1
            elif left < right:
                result = max(dp(left-1), dp(right))
            else:
                result = max(dp(left-1), dp(right-1)) + 1
        memo[i] = result
        return result

    print(max(0, dp(n-1)))
