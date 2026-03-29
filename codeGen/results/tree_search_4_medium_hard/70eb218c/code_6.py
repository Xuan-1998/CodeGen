from collections import defaultdict

def min_operations(n, x):
    memo = defaultdict(lambda: float('inf'))
    memo[(0, n)] = 0 if n >= 1 else -1
    memo[(10**n, n)] = 0

    def helper(x, n):
        if x == 0 and n > 0:
            return float('inf')
        if (x, n) in memo:
            return memo[(x, n)]
        
        last_digit = int(str(x)[-1])
        if last_digit != 0:
            new_x = 10*x + last_digit
            op1 = helper(new_x, n-1)
            op2 = 1 + helper(x // 10, n-1) if x >= 10 else float('inf')
            memo[(x, n)] = min(op1, op2) if op1 != float('inf') and op2 != float('inf') else -1
        else:
            memo[(x, n)] = -1
        
        return memo[(x, n)]

    result = helper(x, n)
    print(result)

if __name__ == "__main__":
    n, x = map(int, input().split())
    min_operations(n, x)
