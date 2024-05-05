memo = {}
def dp(n, k):
    if (n, k) in memo:
        return memo[(n, k)]
    
    if k < n:
        return -1
    
    last_digit = int(str(x)[k-1])
    if last_digit != 0 and n >= len(str(x)):
        new_k = k - 1
        res = dp(n, new_k)
        if res == -1:
            memo[(n, k)] = -1
            return -1
        else:
            memo[(n, k)] = res + 1
            return memo[(n, k)]
    else:
        memo[(n, k)] = -1
        return -1

def solve():
    n, x = map(int, input().split())
    x_str = str(x)
    k = len(x_str)
    
    if k < n:
        print(-1)
    else:
        res = dp(n, k)
        print(res)

solve()
