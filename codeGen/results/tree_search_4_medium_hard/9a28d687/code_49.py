import sys

# Read input from stdin
n = int(input())
costs = [0] * n
strings = [input().strip() for _ in range(n)]

dp = {}

def process(i):
    if (i, strings[i-1]) in dp:
        return dp[(i, strings[i-1])]
    
    res = sys.maxsize

    for j in range(i):
        if strings[j] == strings[i-1]:
            res = min(res, process(j))
        else:
            prefix_cost = 0
            for k in range(len(strings[j])):
                if strings[j][k:] != strings[i-1][k:]:
                    prefix_cost += costs[i-1]
                    break
            res = min(res, process(j) + prefix_cost)

    dp[(i, strings[i-1])] = res
    return res

print(process(n))
