def min_operations(n, x):
    memo = {}

    def rec(x):
        if (n, x) in memo:
            return memo[(n, x)]
        if len(str(x)) == n:
            return 0
        if str(x)[-1] == '0':
            result = 0
        else:
            min_ops = float('inf')
            for y in range(10):
                if y * (x % 10) // 10 + (y * 10) % 10 != x:
                    continue
                min_ops = min(min_ops, rec(y * x))
            result = min_ops + 1
        memo[(n, x)] = result
        return result

    if n > len(str(x)):
        return -1
    return rec(x)

import sys
input = lambda: [int(x) for x in input().split()]
n, x = input()
print(min_operations(n, x))
