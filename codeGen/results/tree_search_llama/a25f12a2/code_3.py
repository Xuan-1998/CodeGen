def solve():
    heads, tails = map(int, input().split())
    
    for i in range(min(heads, tails), 0, -1):
        if (heads - i) + (tails - i) == min(heads, tails):
            return [i, i]
    
    return "No solutions"
