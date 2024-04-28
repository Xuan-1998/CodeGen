def solve(n):
    res = []
    for i in range(2**n):
        perm = [i >> j & 1 for j in range(n)]
        winning_team = True
        for j in range(n-1):
            if (perm[j] == 0 and perm[j+1] > perm[j]):
                winning_team = False
                break
        if winning_team:
            res.append(perm)
    return sorted(res)

n = int(input())
print(*solve(n), sep='\n')
