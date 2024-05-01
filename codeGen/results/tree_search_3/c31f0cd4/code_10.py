from collections import defaultdict

def find_sums(a):
    n = len(a)
    dp = {0: set([0])}
    
    for i in range(n):
        new_dp = defaultdict(set)
        for j, k in list(dp.items()):
            new_dp[j + a[i]].add(k + a[i])
            if j != 0:
                new_dp[k].add(j)
        dp = dict(new_dp)
    
    return sorted(list(set(sum(i) for i in dp.values())))

n = int(input())
a = [int(x) for x in input().split()]
print(' '.join(map(str, find_sums(a))))
