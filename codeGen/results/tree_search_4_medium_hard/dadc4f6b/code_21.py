import heapq
from collections import defaultdict

def solution():
    n, q = map(int, input().split())
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))
    
    memo = {}
    total_brightnesses = []
    pq = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        
        # Calculate the initial brightness
        visible_stars = 0
        for i, (x, y, s) in enumerate(stars):
            if x1 <= x <= x2 and y1 <= y <= y2:
                heapq.heappush(pq, (-s, i))
                visible_stars += s
        
        # Calculate the total brightness
        total_brightness = 0
        while pq and (pq[0][0] < -c or (x1 <= stars[pq[0][1]][0] <= x2 and y1 <= stars[pq[0][1]][1] <= y2)):
            _, i = heapq.heappop(pq)
            total_brightness -= stars[i][2]
        
        # Update the memoized table
        state = (x1, y1, x2, y2)
        if state not in memo:
            memo[state] = visible_stars + total_brightness
        
        total_brightnesses.append(memo[state])
    
    print(*total_brightnesses, sep='\n')

if __name__ == '__main__':
    solution()
