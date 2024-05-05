from math import log10

def min_operations(n, x):
    memo = {}

    def rec(x, n):
        if len(str(x)) == n:
            return 0
        if (len(str(x)), n) in memo:
            return memo[(len(str(x)), n)]
        if n <= 1 or n > 19:
            return -1
        min_ops = float('inf')
        for digit in range(10):
            new_x = x * 10 + digit
            ops = rec(new_x, n)
            if ops != -1 and len(str(new_x)) == n:
                min_ops = min(min_ops, ops + 1)
        memo[(len(str(x)), n)] = min_ops if min_ops != float('inf') else -1
        return memo[(len(str(x)), n)]

    return rec(x, n)

if __name__ == "__main__":
    while True:
        try:
            n, x = map(int, input().split())
            print(min_operations(n, x))
        except ValueError:
            break
