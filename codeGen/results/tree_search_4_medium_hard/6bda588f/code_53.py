from collections import defaultdict

def min_f(n, s, a):
    memo = defaultdict(int)

    def dp(i, shift):
        if (i, shift) in memo:
            return memo[(i, shift)]
        
        if i == 0:
            return a[0] * (1 - abs(shift))

        res = float('inf')
        for x, y in [(0, a[i-1]-shift), (a[i-1]-shift, 0)]:
            res = min(res, dp(i-1, shift-x-y))
        
        memo[(i, shift)] = res
        return res

    return int(min_f(n, s, [int(x) for x in input().split()][1:]))
