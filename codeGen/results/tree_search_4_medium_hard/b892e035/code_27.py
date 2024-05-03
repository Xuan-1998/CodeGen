def dp(n, p0, p1):
    memo = {}

    def rec(i, seen):
        if i == n:
            return 1
        if (i, seen) in memo:
            return memo[(i, seen)]
        
        res = 0
        if not seen & (2 ** p0[0]):
            res += p0[0] * p0[1] * rec(i + 1, seen | 2 ** p0[0])
        if not seen & (2 ** p1[0]):
            res += p1[0] * p1[1] * rec(i + 1, seen | 2 ** p1[0])
        
        memo[(i, seen)] = res
        return res

    total_prob = 0
    for i in range(n):
        if not (seen := (2 ** p0[i]) | (2 ** p1[i])):
            total_prob += rec(i + 1, seen)
    
    return round(total_prob, 6)


T = int(input())
for _ in range(T):
    n = int(input())
    p0 = [(*map(int, input().split()), *map(int, input().split())) for _ in range(n)]
    p1 = [(*map(int, input().split()), *map(int, input().split())) for _ in range(n)]
    
    print(dp(n, p0, p1))
