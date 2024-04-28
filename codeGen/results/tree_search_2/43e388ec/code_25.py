import sys

dp = {}

def f(a, b, i):
    if (a & b, i) in dp:
        return dp[(a & b, i)]
    
    if a == 0 or b == 0:
        return 0
    
    result = 0
    while a and b:
        if a & 1 and b & 1:
            result += f(a >> 1, b >> 1, i + 1)
        else:
            result += (a & 1) ^ (b & 1)
        a >>= 1
        b >>= 1
    
    dp[(a & b, i)] = result
    return result

a, b = map(int, input().split())
print((f(a, b, 0)) % (10**9 + 7))
