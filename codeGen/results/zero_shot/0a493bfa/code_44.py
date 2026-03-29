import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

heap = []

for x in a:
    for y in a:
        if y > x and gcd(x, y) not in b:
            heapq.heappush(heap, -gcd(x, y))

max_beauty = 0
while heap:
    x = -heapq.heappop(heap)
    max_beauty += x

print(max_beauty)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
