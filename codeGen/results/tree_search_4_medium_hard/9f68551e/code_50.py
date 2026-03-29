import heapq

def min_mana(monsters, times, healths):
    dp = [[float('inf')] * (max(times) + 1) for _ in range(max(monsters) + 1)]
    
    pq = [(0, 0)]  # priority queue to keep track of monsters and their appearance times
    
    for i in range(1, max(monsters) + 1):
        while pq[0][1] < times[i - 1]:
            mana, _ = heapq.heappop(pq)
        
        dp[i][times[i - 1]] = min(dp[i - 1][times[i - 2]], mana + healths[i - 1])
    
    return dp[-1][-1]

# Test the function
monsters = [int(i) for i in input().split()]
times = [int(i) for i in input().split()]
healths = [int(i) for i in input().split()]

print(min_mana(monsters, times, healths))
