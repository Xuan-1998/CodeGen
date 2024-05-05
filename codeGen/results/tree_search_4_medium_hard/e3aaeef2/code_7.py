def solve(n, m):
    MOD = 10**9 + 7
    memo = {}

    def helper(length, value):
        if (length, value) in memo:
            return memo[(length, value)]
        if length == 0:
            return value
        next_value = sum(int(digit) + 1 for digit in str(value)) % MOD
        result = helper(length - 1, next_value)
        memo[(length, value)] = result
        return result

    return helper(len(str(n)), n) % MOD


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
