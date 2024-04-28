from collections import defaultdict

def max_points(a):
    n = len(a)
    dp = defaultdict(int)
    
    for i in range(n):
        if i > 0:
            for j in range(i):
                last_seen = a[j]
                current_sum = sum(a[:i+1])
                if (last_seen, current_sum) in dp:
                    dp[(last_seen, current_sum)] = max(dp[(last_seen, current_sum)], dp[(a[i], current_sum - last_seen)])
                else:
                    dp[(last_seen, current_sum)] = 0
        
    return max(dp.values())

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
