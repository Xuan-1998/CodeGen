import heapq
n = int(input())
costs = []
strings = []

for _ in range(n):
    cost, s = input().split()
    cost = int(cost)
    strings.append(s)
    costs.append((cost, s))

heapq.heapify(costs)

ans = 0

while len(strings) > 1:
    c1, s1 = heapq.heappop(costs)
    c2, s2 = heapq.heppop(costs)
    
    if s1 < s2:
        ans += c1
        strings.remove(s1)
    elif s1 > s2:
        ans += c2
        strings.remove(s2)
    else:
        break

if len(strings) > 0:
    print(-1)
else:
    print(ans)
