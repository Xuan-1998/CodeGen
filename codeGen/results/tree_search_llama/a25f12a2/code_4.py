def solve(heads, tails):
    if heads + tails == 0:
        return ["No solutions"]
    
    for h in range(1, min(heads, tails) // 2 + 1):
        t = (heads - h) // 2
        if h * 2 + t * 3 == heads and h * 2 + t * 2 == tails:
            return [h, t]
    
    for t in range(1, min(heads, tails) // 2 + 1):
        h = (tails - t) // 2
        if h * 2 + t * 3 == heads and h * 2 + t * 2 == tails:
            return [h, t]
    
    return ["No solutions"]

heads = int(input())
tails = int(input())

result = solve(heads, tails)
print(result)
