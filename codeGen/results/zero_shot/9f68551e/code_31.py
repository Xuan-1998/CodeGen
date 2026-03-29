import heapq
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    monsters = []
    for _ in range(n):
        k, h = map(int, sys.stdin.readline().split())
        monsters.append((k, h))

    monsters.sort()
    heap = [(0, 0)]  # initial mana and damage
    total_mana = 0

    for k, h in monsters:
        while heap[0][1] < h:  # if the current damage is not enough to kill the monster
            mana, damage = heapq.heappop(heap)
            mana += damage + 1  # increase the mana by the damage and add 1
            total_mana += mana  # update the total mana

        heapq.heappush(heap, (mana, h))  # push the updated mana and health back into the heap

    print(total_mana)  # print the least amount of mana required to kill all monsters
