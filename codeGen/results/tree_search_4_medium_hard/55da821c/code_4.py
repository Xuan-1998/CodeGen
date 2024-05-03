import sys

def min_replants():
    n, m = map(int, input().split())
    dp = {}
    for i in range(m):
        dp[(i, 0)] = 0
        dp[(m, i+1)] = i+1
    
    for _ in range(n):
        s, x = map(int, input().split())
        section, replanted = (s-1, max(dp.keys())[0]) if s > 1 else (-1, min(dp.keys())[0])
        
        while True:
            if section == s - 1:
                dp[(section+1, replanted+1)] = min(dp.get((section+1, replanted), float('inf')), dp[(section, replanted)] + 1)
                break
            else:
                for i in range(section-1, -1, -1):
                    if (i+1, replanted+1) not in dp:
                        dp[(i+1, replanted+1)] = min(dp.get((i+1, replanted), float('inf')), dp[(i, replanted)] + 1)
                        break
                section += 1
        
    return min(dp.values()) - 1

print(min_replants())
