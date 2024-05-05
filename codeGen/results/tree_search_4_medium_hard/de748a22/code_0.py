def sign_variable_sum(arr):
    total = 0
    for x in arr:
        if x > 0:
            total += 1
        elif x < 0:
            total -= 1
    return total

def solve(arr, q):
    n = len(arr)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    signs = {'+': 1, '-': -1}

    for i in range(1, n + 1):
        if arr[i - 1] > 0:
            include_sum = sign_variable_sum(arr[:i]) - 1
            exclude_sum = dp[i - 1]
            dp[i] = min(dp[i - 1], (include_sum if include_sum >= 0 else float('inf')) + 1)
        elif arr[i - 1] < 0:
            include_sum = sign_variable_sum(arr[:i]) + 1
            exclude_sum = dp[i - 1]
            dp[i] = min(dp[i - 1], (exclude_sum if exclude_sum >= 0 else float('inf')))

    res = []
    for l, r in q:
        res.append(min(dp[r] - dp[l - 1]) + 1)
    return res

# Example usage
n, q = map(int, input().split())
arr = list(input())
queries = [list(map(int, input().split())) for _ in range(q)]
print(*solve(arr, queries), sep='\n')
