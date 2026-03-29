import heapq

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    pq = []
    sum = 0
    for i in range(n - 1, -1, -1):
        heapq.heappush(pq, -arr[i])
        sum += -heapq.heappop(pq)
    print(sum)

solve()

