def solve(n, m):
    memo = {(1, x): 0 if x < 10 else 1 for x in range(11)}

    def dp(length, value):
        if (length, value) not in memo:
            if length > 1:
                new_length = length
                new_value = sum(int(digit) + 1 for digit in str(value))
                memo[(length, value)] = dp(new_length, new_value)
            else:
                memo[(length, value)] = 0 if value < 10 else 1

        return memo[(length, value)]

    return dp(len(str(n)), n)[2]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
