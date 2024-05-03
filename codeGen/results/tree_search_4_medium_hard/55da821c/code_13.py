from collections import defaultdict

def min_replants(n, m):
    # Initialize memoization table
    dp = {(0, [False] * m): 0}

    for i in range(1, n+1):
        replanted = 0
        species = list(dp.keys())[-1][1]
        for j in range(m-1, -1, -1):
            if i <= len([x[1].index(True) + 1 for x in dp.values() if not x[1]][j]):
                break
            replanted += 1
            species[j] = True
        dp[(replanted, tuple(species))] = replanted

    return list(dp.keys())[-1][0]

n, m = map(int, input().split())
print(min_replants(n, m))
