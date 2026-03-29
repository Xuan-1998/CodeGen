import heapq

def solve():
    n, q, c = map(int, input().split())
    
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))
    
    dp = [[0] * 101 for _ in range(1000001)]
    memo = {}
    
    for i, (x, y, s) in enumerate(stars):
        for t in range(max(s + c - 1, 0), 1000000):
            dp[t][max(x, min(y, 100))] += s
            if dp[t][x] > c:
                dp[t][x] = c
    
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        
        heap = []
        for i in range(max(y1 - 1, 0), min(y2, 100)):
            for j in range(max(x1 - 1, 0), min(x2, 100)):
                if dp[t][j] > c:
                    heapq.heappush(heap, (dp[t][j], i, j))
        
        total_brightness = 0
        while heap and (heap[0][1], heap[0][2]) <= (y2, x2):
            brightness, _, _ = heapq.heappop(heap)
            total_brightness += brightness
        
        print(total_brightness)

if __name__ == "__main__":
    solve()
