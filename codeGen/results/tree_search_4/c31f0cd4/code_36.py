from collections import defaultdict

def get_distinct_sums(n):
    arr = list(map(int, input().split()))
    dp = defaultdict(int)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == j:
                dp[j] += 1
            else:
                for k in range(j - 1, -1, -1):
                    dp[k] = (dp.get(k, 0) or 0) + (dp.get(k - i, 0) or 0)
    
    return ' '.join(map(str, sorted(dp.keys())))

n = int(input())
print(get_distinct_sums(n))
