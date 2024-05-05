import heapq

n, _, _ = map(int, input().split())
monsters = []
for _ in range(n):
    k_i, h_i = map(int, input().split())
    monsters.append((k_i, h_i))

heap = [(0, 0)]  # (mana, seconds_left)
total_mana = 0
for _, h_i in sorted(monsters, key=lambda x: x[0]):
    while heap:
        mana, seconds_left = heapq.heappop(heap)
        if mana >= h_i:
            total_mana += mana - (h_i - 1) if h_i > 1 else 0
            break
        elif seconds_left < _:
            break
        else:
            heapq.heappush(heap, (mana + 1, seconds_left - 1))
    else:
        print(-1)
        exit()

print(total_mana)
