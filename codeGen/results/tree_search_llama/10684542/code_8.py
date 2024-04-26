import math

def getExponent(n, p):
    if p <= 1:
        return None
    
    max_power = int(math.log2(n)) // math.log2(p)
    
    for x in range(max_power, -1, -1):
        if pow(p, x) > n:
            return x-1
    return max_power

n, p = map(int, input().split())
print(getExponent(n, p))
